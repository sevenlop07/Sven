--[[ harvest_extract.lua — Sven Roblox asset harvester, Studio side (runtime-neutral; driven by tools/harvest_assets.py).

Loaded once per Studio session through execute_luau; it installs _G.SvenHarvest:
  SvenHarvest.sanitize(model)            strip every script / remote / GUI / sound / click & prompt object → {removed=N, classes={...}}
  SvenHarvest.prepare(path, opts)         sanitize + extract the model at `path` ("workspace._AssetHarvest.Foo") into a JSON
                                          string kept in memory → short JSON summary {key, bytes, parts, meshes, meshFail, texFail}
  SvenHarvest.page(key, i, n)             substring [i, i+n) of the prepared JSON (execute_luau returns are capped near 100k chars)
  SvenHarvest.drop(key)                   free the buffer

JSON written (read by studio_kit/roblox_json_to_glb.py build_from_json):
  { name, meshes = { [key] = { v = {x,y,z,...} (centred on the mesh bounds), f = {a,b,c,...} (0-based),
                               ext = {sx,sy,sz} (mesh bounds), c = {0xRRGGBB per vertex} | nil } },
    parts  = { { n, sz, cf (12 numbers, relative to the model pivot), col, mat, tr, ref, shape,
                 mid (mesh key) | nil, ms (SpecialMesh FileMesh scale) | nil, smType, smScale } } }
Vertex colours are sampled from the part's TextureID / SurfaceAppearance.ColorMap at each vertex UV when Studio lets
us open the image; otherwise the part keeps its flat Color. Everything is read-only apart from the sanitize step.
]]
local HttpService = game:GetService("HttpService")
local AssetService = game:GetService("AssetService")

local H = _G.SvenHarvest or {}
_G.SvenHarvest = H
H.buf = H.buf or {}

H.BANNED = {
	"Script", "LocalScript", "ModuleScript", "RemoteEvent", "RemoteFunction", "UnreliableRemoteEvent",
	"BindableEvent", "BindableFunction", "ScreenGui", "BillboardGui", "SurfaceGui", "Sound",
	"ClickDetector", "ProximityPrompt", "Tool", "Humanoid",
}

local function r3(x) return math.floor(x * 1000 + 0.5) / 1000 end

function H.sanitize(m)
	local removed, classes = 0, {}
	for _, d in ipairs(m:GetDescendants()) do
		if d.Parent then
			for _, cls in ipairs(H.BANNED) do
				if d:IsA(cls) then
					classes[d.ClassName] = (classes[d.ClassName] or 0) + 1
					removed += 1
					d:Destroy()
					break
				end
			end
		end
	end
	return { removed = removed, classes = classes }
end

local function resolve(path)
	local node = game
	for seg in string.gmatch(path, "[^%.]+") do
		if seg ~= "game" then
			node = node and node:FindFirstChild(seg)
		end
	end
	return node
end

-- texture → pixel reader (or nil)
local imgCache = {}
local function openImage(texId)
	if texId == nil or texId == "" then return nil end
	if imgCache[texId] ~= nil then return imgCache[texId] or nil end
	local ok, img = pcall(function()
		return AssetService:CreateEditableImageAsync(Content.fromUri(texId))
	end)
	if not ok or not img then
		imgCache[texId] = false
		return nil
	end
	local size = img.Size
	local okb, buf = pcall(function() return img:ReadPixelsBuffer(Vector2.zero, size) end)
	img:Destroy()
	if not okb then
		imgCache[texId] = false
		return nil
	end
	local rec = { w = size.X, h = size.Y, buf = buf }
	imgCache[texId] = rec
	return rec
end

local function sample(img, u, v)
	u = u - math.floor(u)
	v = v - math.floor(v)
	local x = math.clamp(math.floor(u * img.w), 0, img.w - 1)
	local y = math.clamp(math.floor(v * img.h), 0, img.h - 1)
	local o = (y * img.w + x) * 4
	local r, g, b = buffer.readu8(img.buf, o), buffer.readu8(img.buf, o + 1), buffer.readu8(img.buf, o + 2)
	return r * 65536 + g * 256 + b
end

local function readMesh(meshId, img)
	local ok, em = pcall(function()
		return AssetService:CreateEditableMeshAsync(Content.fromUri(meshId))
	end)
	if not ok or not em then return nil, tostring(em) end
	local ids = em:GetVertices()
	local index, pos = {}, {}
	local mn = Vector3.new(math.huge, math.huge, math.huge)
	local mx = -mn
	for i, vid in ipairs(ids) do
		index[vid] = i - 1
		local p = em:GetPosition(vid)
		pos[i] = p
		mn = mn:Min(p)
		mx = mx:Max(p)
	end
	local ctr = (mn + mx) * 0.5
	local v = table.create(#ids * 3)
	for i, p in ipairs(pos) do
		local q = p - ctr
		v[#v + 1] = r3(q.X); v[#v + 1] = r3(q.Y); v[#v + 1] = r3(q.Z)
	end
	local f, colours = {}, nil
	if img then colours = table.create(#ids, -1) end
	for _, fid in ipairs(em:GetFaces()) do
		local fv = em:GetFaceVertices(fid)
		if #fv == 3 then
			f[#f + 1] = index[fv[1]]; f[#f + 1] = index[fv[2]]; f[#f + 1] = index[fv[3]]
			if colours then
				local okuv, uvs = pcall(function() return em:GetFaceUVs(fid) end)
				if okuv and uvs and #uvs == 3 then
					for k = 1, 3 do
						local vi = index[fv[k]] + 1
						if colours[vi] == -1 then
							local uv = em:GetUV(uvs[k])
							colours[vi] = sample(img, uv.X, uv.Y)
						end
					end
				end
			end
		end
	end
	em:Destroy()
	if colours then
		for i = 1, #colours do if colours[i] == -1 then colours[i] = 0xFFFFFF end end
	end
	local ext = mx - mn
	return { v = v, f = f, ext = { r3(ext.X), r3(ext.Y), r3(ext.Z) }, c = colours }
end

function H.prepare(path, opts)
	opts = opts or {}
	local m = resolve(path)
	if not m then return HttpService:JSONEncode({ error = "not found: " .. path }) end
	local san = H.sanitize(m)
	local piv = m:IsA("Model") and m:GetPivot() or (m:IsA("BasePart") and m.CFrame or CFrame.new())
	local parts, meshes = {}, {}
	local meshFail, texFail, failed, unions, fallback = 0, 0, {}, 0, 0
	local list = m:GetDescendants()
	if m:IsA("BasePart") then table.insert(list, m) end
	for _, d in ipairs(list) do
		if d:IsA("BasePart") and d.Transparency < 0.98 then
			local rel = piv:ToObjectSpace(d.CFrame)
			local x, y, z, r00, r01, r02, r10, r11, r12, r20, r21, r22 = rel:GetComponents()
			local c = d.Color
			local e = {
				n = d.Name,
				sz = { r3(d.Size.X), r3(d.Size.Y), r3(d.Size.Z) },
				cf = { r3(x), r3(y), r3(z), r3(r00), r3(r01), r3(r02), r3(r10), r3(r11), r3(r12), r3(r20), r3(r21), r3(r22) },
				col = { math.floor(c.R * 255 + 0.5), math.floor(c.G * 255 + 0.5), math.floor(c.B * 255 + 0.5) },
				mat = d.Material.Name,
				tr = r3(d.Transparency),
				ref = r3(d.Reflectance),
				shape = d:IsA("WedgePart") and "Wedge" or (d:IsA("Part") and d.Shape.Name or "Block"),
			}
			if d:IsA("PartOperation") then unions += 1 end -- union/negate geometry is not readable: box fallback
			local meshId, tex = "", ""
			local sm = d:FindFirstChildOfClass("SpecialMesh")
			if d:IsA("MeshPart") then
				meshId = d.MeshId
				tex = d.TextureID
				local sa = d:FindFirstChildOfClass("SurfaceAppearance")
				if sa then
					local okc, cm = pcall(function() return sa.ColorMap end)
					if okc and cm and cm ~= "" then tex = cm end
				end
			elseif sm then
				e.smType = sm.MeshType.Name
				e.smScale = { r3(sm.Scale.X), r3(sm.Scale.Y), r3(sm.Scale.Z) }
				if sm.MeshType == Enum.MeshType.FileMesh and sm.MeshId ~= "" then
					meshId = sm.MeshId
					tex = sm.TextureId
					e.ms = e.smScale
				end
			end
			if meshId ~= "" then
				local key = meshId .. "|" .. tex
				if meshes[key] == nil then
					local img = (opts.textures ~= false) and openImage(tex) or nil
					if tex ~= "" and not img then texFail += 1 end
					local md, err = readMesh(meshId, img)
					if md then
						meshes[key] = md
					else
						meshes[key] = false
						meshFail += 1
						failed[#failed + 1] = meshId .. " (" .. string.sub(err or "?", 1, 80) .. ")"
					end
				end
				if meshes[key] then
					e.mid = key
					if meshes[key].c then e.col = { 255, 255, 255 } end
				else
					fallback += 1 -- drawn as its bounding box
				end
			end
			parts[#parts + 1] = e
		end
	end
	local outMeshes = {}
	for k, md in pairs(meshes) do if md then outMeshes[k] = md end end
	local key = opts.key or m.Name
	local json = HttpService:JSONEncode({ name = key, meshes = outMeshes, parts = parts })
	H.buf[key] = json
	imgCache = {}
	local nMesh = 0
	for _ in pairs(outMeshes) do nMesh += 1 end
	local ext = m:IsA("Model") and m:GetExtentsSize() or m.Size
	return HttpService:JSONEncode({
		key = key, bytes = #json, parts = #parts, meshes = nMesh, meshFail = meshFail, texFail = texFail, unions = unions, fallback = fallback,
		failed = failed, sanitized = san, extentStuds = { r3(ext.X), r3(ext.Y), r3(ext.Z) },
	})
end

function H.page(key, i, n)
	local s = H.buf[key]
	if not s then return "" end
	return string.sub(s, i, i + n - 1)
end

function H.drop(key)
	H.buf[key] = nil
	return "ok"
end

return "SvenHarvest ready"
