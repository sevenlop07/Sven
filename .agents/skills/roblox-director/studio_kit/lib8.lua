-- lib8: render quality, contact checks (nothing may pass through anything) and simple real physics helpers.
local MT = shared.MT
local rad = math.rad

-- 1. quality: max editor quality, full mesh detail, render everything before a frame is shown
function MT.quality()
	local r = settings().Rendering
	local out = {}
	for k, v in pairs({ EditQualityLevel = Enum.QualityLevel.Level21, QualityLevel = Enum.QualityLevel.Level21,
		MeshPartDetailLevel = Enum.MeshPartDetailLevel.Level04, EagerBulkExecution = true }) do
		local ok, e = pcall(function() r[k] = v end)
		table.insert(out, k .. (ok and "=ok" or ("=ERR " .. tostring(e))))
	end
	return table.concat(out, " ")
end

-- 2. clipping: shrink each body part a little (so touching is fine) and look for anything inside it.
local BODY = { "torso", "head", "armL", "armR", "legL", "legR" }
local SOFT = { ground = true, floor = true, path = true, road = true, grass = true, water = true, rug = true, carpet = true, riverbed = true, sand = true }
local function soft(p)
	local n = p.Name:lower()
	for k in pairs(SOFT) do if n:find(k) then return true end end
	return p.Transparency >= 0.95
end
function MT.clips(inset)
	inset = inset or 0.18
	local hits = {}
	local rigModels = {}
	local restore = {}
	for _, p in ipairs(MT.root():GetDescendants()) do if p:IsA("BasePart") and not p.CanQuery then p.CanQuery = true; table.insert(restore, p) end end
	for name, rig in pairs(MT.rigs) do rigModels[rig.model] = name end
	for name, rig in pairs(MT.rigs) do
		local params = OverlapParams.new()
		params.FilterType = Enum.RaycastFilterType.Exclude
		params.FilterDescendantsInstances = { rig.model }
		for _, k in ipairs(BODY) do
			local p = rig[k]
			if p and p.Transparency < 0.95 then
				local sz = p.Size - Vector3.new(inset, inset, inset) * 2
				if sz.X > 0.05 and sz.Y > 0.05 and sz.Z > 0.05 then
					for _, q in ipairs(workspace:GetPartBoundsInBox(p.CFrame, sz, params)) do
						if not soft(q) then
							local m = q:FindFirstAncestorOfClass("Model")
							local who = m and rigModels[m]
							local held = false
							for _, e in ipairs(rig.extra) do if e[1] == q then held = true end end
							if not held then table.insert(hits, name .. "." .. k .. " x " .. (who and (who .. ".") or "") .. q.Name) end
						end
					end
				end
			end
		end
	end
	for _, p in ipairs(restore) do p.CanQuery = false end
	return hits
end
-- ground contact: a standing rig's lowest leg point should be within 0.15 of the floor under it
function MT.floating()
	local bad = {}
	for name, rig in pairs(MT.rigs) do
		if not rig.lie and (rig.lift or 0) == 0 and rig.legL then
			local low = math.min(rig.legL.Position.Y, rig.legR.Position.Y) - rig.legL.Size.Y / 2
			local params = RaycastParams.new(); params.FilterType = Enum.RaycastFilterType.Exclude; params.FilterDescendantsInstances = { rig.model }
			local hit = workspace:Raycast(rig.legL.Position, Vector3.new(0, -50, 0), params)
			if hit and math.abs(hit.Position.Y - low) > 0.15 then table.insert(bad, string.format("%s %.2f", name, low - hit.Position.Y)) end
		end
	end
	return bad
end

-- 3. physics helpers (Roblox gravity is 196.2 studs/s^2; we use a softer 60 so throws read on screen at 30 fps)
MT.G = 60
-- thrown object: from a to b (shot coords) between frames f0..f1, peak height h above the higher end; spins as it flies
function MT.toss(part, f, f0, f1, a, b, h, spin)
	if f < f0 then return false end
	local t = math.clamp((f - f0) / math.max(1, f1 - f0), 0, 1)
	local A, B = MT.V(a[1], a[2], a[3]), MT.V(b[1], b[2], b[3])
	local y = A.Y + (B.Y - A.Y) * t + 4 * (h or 2) * t * (1 - t)
	local p = A:Lerp(B, t)
	part.CFrame = CFrame.new(p.X, y, p.Z) * CFrame.Angles(rad((spin or 540) * t), rad((spin or 540) * 0.4 * t), 0)
	return t >= 1
end
-- dropped object: falls with gravity from height, then 2 small bounces losing 60% each time, then rests
function MT.drop(part, f, f0, at, h0, restY)
	local t = math.max(0, (f - f0) / 30)
	local y0, g = h0, MT.G
	local y, v = y0, 0
	local tFall = math.sqrt(2 * (y0 - restY) / g)
	if t < tFall then y = y0 - 0.5 * g * t * t
	else
		local vImp = g * tFall; t = t - tFall; y = restY
		for _ = 1, 2 do
			vImp = vImp * 0.4; local tb = 2 * vImp / g
			if t < tb then y = restY + vImp * t - 0.5 * g * t * t; break end
			t = t - tb
		end
	end
	local p = MT.V(at[1], at[2], 0)
	part.CFrame = CFrame.new(p.X, y, p.Z) * (part.CFrame - part.CFrame.Position)
end
-- squash and settle for a landing body (jump/fall): returns a scale-like dip 0..1 for the frames after impact
function MT.settle(f, fImpact, len) local t = (f - fImpact) / (len or 8); if t < 0 or t > 1 then return 0 end; return math.sin(t * math.pi) * (1 - t) end


-- 4. auto-resolve after every shot build: arms out of their own body, then push rigs apart (crowd yields to cast),
--    rigs out of props, lying rigs up out of beds/floors. Nothing passes through anything.
local function boxHits(p, params, inset)
	local sz = p.Size - Vector3.one * 2 * inset
	if sz.X <= 0.05 or sz.Y <= 0.05 or sz.Z <= 0.05 then return {} end
	return workspace:GetPartBoundsInBox(p.CFrame, sz, params)
end
local function deep(t) local o = {}; for k, v in pairs(t or {}) do o[k] = type(v) == "table" and table.clone(v) or v end; return o end
local function selfFix(name)
	local rig = MT.rigs[name]
	if not rig.torso or not rig.armL then return end
	for _, side in ipairs({ "L", "R" }) do
		local arm, key = rig["arm" .. side], "arm_" .. side
		local inc = OverlapParams.new(); inc.FilterType = Enum.RaycastFilterType.Include
		inc.FilterDescendantsInstances = { rig.torso }
		local ex = OverlapParams.new(); ex.FilterType = Enum.RaycastFilterType.Exclude
		local skipList = { rig.model }
		for _, e in ipairs(rig.extra) do table.insert(skipList, e[1]) end
		ex.FilterDescendantsInstances = skipList
		local function bad()
			MT.apply(name)
			local L = arm.Size.Y
			if #workspace:GetPartBoundsInBox(arm.CFrame * CFrame.new(0, -L * 0.2, 0), Vector3.new(arm.Size.X - 0.2, L * 0.55, arm.Size.Z - 0.2), inc) > 0 then return true end
			for _, q in ipairs(boxHits(arm, ex, 0.15)) do if not soft(q) and q.Name ~= "Handle" then return true end end
			return false
		end
		if bad() then
			local a0 = rig.pose[key] and table.clone(rig.pose[key]) or { 0, 0, 0 }
			local fixed = false
			for d = 5, 70, 5 do
				for _, c in ipairs({ { d, 0, 0 }, { 0, -d, 0 }, { 0, 0, d }, { d, -d, 0 }, { -d, 0, 0 }, { 0, -d, d } }) do
					rig.pose[key] = { (a0[1] or 0) + c[1], (a0[2] or 0) + c[2], (a0[3] or 0) + c[3] }
					if not bad() then fixed = true; break end
				end
				if fixed then break end
			end
			if not fixed then rig.pose[key] = a0; MT.apply(name); rig.armStuck = true end
		end
	end
end
function MT.resolve()
	local restore = {}
	for _, p in ipairs(MT.root():GetDescendants()) do if p:IsA("BasePart") and not p.CanQuery then p.CanQuery = true; table.insert(restore, p) end end
	local rigModels, names = {}, {}
	for name, rig in pairs(MT.rigs) do rigModels[rig.model] = name; table.insert(names, name) end
	table.sort(names)
	for _, name in ipairs(names) do selfFix(name) end
	local total = {}
	local iters = 0
	for iter = 1, 40 do
		iters = iter
		local push, any = {}, false
		for _, name in ipairs(names) do
			local rig = MT.rigs[name]
			local ex = OverlapParams.new(); ex.FilterType = Enum.RaycastFilterType.Exclude
			local skipList = { rig.model }
			for _, e in ipairs(rig.extra) do table.insert(skipList, e[1]) end
			ex.FilterDescendantsInstances = skipList
			for _, k in ipairs(BODY) do
				local p = rig[k]
				if p and p.Transparency < 0.95 and (rig.armStuck or (k ~= "armL" and k ~= "armR")) then
					for _, q in ipairs(boxHits(p, ex, 0.15)) do
						if not soft(q) and q.Name ~= "Handle" then
							local m = q:FindFirstAncestorOfClass("Model")
							local other = m and rigModels[m]
							local heldElsewhere = false
							if other then for _, e in ipairs(MT.rigs[other].extra) do if e[1] == q and e[2] ~= "head" then heldElsewhere = true end end end
							local d, w
							if other then
								d = rig.pos - MT.rigs[other].pos
								local mc, oc = name:match("^x") ~= nil, other:match("^x") ~= nil
								w = (mc and not oc) and 1 or ((oc and not mc) and 0 or 0.5)
							else
								d = p.Position - q.Position; w = 1
							end
							d = Vector3.new(d.X, 0, d.Z)
							if d.Magnitude < 1e-3 then d = Vector3.new(1, 0, 0) end
							if w > 0 then
								if rig.lie then push[name] = (push[name] or Vector3.zero) + Vector3.new(0, 0.08, 0)
								else push[name] = (push[name] or Vector3.zero) + d.Unit * 0.18 * w end
								any = true
							end
						end
					end
				end
			end
		end
		if not any then break end
		for name, v in pairs(push) do
			local rig = MT.rigs[name]
			if v.Magnitude > 0.3 then v = v.Unit * 0.3 end
			total[name] = (total[name] or Vector3.zero) + v
			local cap = name:match("^x") and 3 or 1.5
			if total[name].Magnitude < cap then rig.pos = rig.pos + v; MT.apply(name) end
		end
	end
	for _, name in ipairs(names) do MT.rigs[name].armStuck = nil; selfFix(name) end
	for _, name in ipairs(names) do
		local rig = MT.rigs[name]
		if rig.base then rig.base.pos = rig.pos; rig.base.pose = deep(rig.pose) end
	end
	for _, p in ipairs(restore) do p.CanQuery = false end
	local moved = {}
	for n, v in pairs(total) do if v.Magnitude > 0.05 then table.insert(moved, string.format("%s %.1f", n, v.Magnitude)) end end
	MT.lastResolve = "iters " .. iters .. " moved: " .. table.concat(moved, ", ")
	return MT.lastResolve
end
local buildBase = MT.buildBase or MT.build
MT.buildBase = buildBase
function MT.build(id)
	buildBase(id)
	if MT.autoResolve ~= false then pcall(MT.resolve) end
end
-- per-frame guard: if idle sway pushes an arm into something, that arm keeps its clean base pose this frame
local frameBase = MT.frameBase or MT.frame
MT.frameBase = frameBase
function MT.frame(id, f)
	frameBase(id, f)
	if MT.armGuard == false then return end
	for name, rig in pairs(MT.rigs) do
		if rig.armL and rig.base and not rig.lie then
			local ex = OverlapParams.new(); ex.FilterType = Enum.RaycastFilterType.Exclude
			local skipList = { rig.model }
			for _, e in ipairs(rig.extra) do table.insert(skipList, e[1]) end
			ex.FilterDescendantsInstances = skipList
			local changed = false
			for _, side in ipairs({ "L", "R" }) do
				local arm = rig["arm" .. side]
				for _, q in ipairs(boxHits(arm, ex, 0.15)) do
					if not soft(q) and q.Name ~= "Handle" then
						local b = rig.base.pose["arm_" .. side]
						rig.pose["arm_" .. side] = b and table.clone(b) or nil
						changed = true
						break
					end
				end
			end
			if changed then MT.apply(name) end
		end
	end
end
-- 5. tiled capture for full 1080x1920 sharpness: odd F = upper half (camera pitched up V/4), even F = lower half.
--    Both tiles share the camera centre, so stitch.py joins them exactly (pure rotation = homography, no parallax).
MT.TILE_MARGIN = 6
function MT.frameTile(id, F)
	local f = math.floor((F + 1) / 2)
	local k = (F % 2 == 1) and 1 or 2
	local cam = workspace.CurrentCamera
	if k == 1 or MT.cur ~= id or not MT.tileBase then
		MT.frame(id, f)
		MT.tileBase = { cam.CFrame, cam.FieldOfView }
	end
	local cf, V = MT.tileBase[1], MT.tileBase[2]
	local d = math.rad(V / 4)
	cam.CameraType = Enum.CameraType.Scriptable
	cam.CFrame = cf * CFrame.Angles(k == 1 and d or -d, 0, 0)
	cam.FieldOfView = V / 2 + MT.TILE_MARGIN
end
function MT.shotFovs()
	local out = {}
	for id in pairs(MT.SHOTS) do
		local ok = pcall(MT.frame, id, 1)
		out[id] = ok and workspace.CurrentCamera.FieldOfView or 0
	end
	return game:GetService("HttpService"):JSONEncode(out)
end
MT.POSES.hug_self = { arm_L = { 75, 5, 0 }, arm_R = { 75, 5, 0 }, head = { 10, 0, 0 } }
MT.POSES.cover_face = { arm_L = { 110, 5, 20 }, arm_R = { 110, 5, 20 }, head = { 12, 0, 0 } }
-- 6. 4K: R pitched captures per frame (shared.MT_TILES from tiles4k.py); F = (frame-1)*R + k
function MT.frameTileN(id, F)
	local T = shared.MT_TILES[id]
	local R = T.rows
	local f = math.floor((F - 1) / R) + 1
	local k = (F - 1) % R + 1
	local cam = workspace.CurrentCamera
	if k == 1 or MT.cur ~= id or not MT.tileBase then
		MT.frame(id, f)
		MT.tileBase = { cam.CFrame, cam.FieldOfView }
	end
	cam.CameraType = Enum.CameraType.Scriptable
	cam.CFrame = MT.tileBase[1] * CFrame.Angles(math.rad(T.p[k]), 0, 0)
	cam.FieldOfView = T.Ft
end
return "lib8 loaded"
