-- MT: Monster Test builder for Roblox Studio (Edit mode). Loaded into shared.MT by the bridge.
-- Coordinates in shot data are the same as the Blender version: (x, y, z) with z up; V() converts to Roblox.
local MT = {}
MT.HEAD = 1.25   -- uniform head scale vs a standard R6 head (hair accessories scale by the same k, so they sit like in-game)
shared.MT = MT
local Lighting = game:GetService("Lighting")
local rad = math.rad

local function V(x, y, z) return Vector3.new(x, z or 0, -y) end
MT.V = V
local function C(h) return Color3.fromHex(h) end
MT.C = C

MT.FACES = shared.MT_FACES or {}
MT.rigs = {}

function MT.root()
	local f = workspace:FindFirstChild("MT")
	if not f then f = Instance.new("Folder"); f.Name = "MT"; f.Parent = workspace end
	return f
end

function MT.clear()
	local f = workspace:FindFirstChild("MT")
	if f then f:Destroy() end
	MT.rigs = {}
	for _, n in ipairs({ "Baseplate", "SpawnLocation", "CLAUDE_HELLO" }) do
		local o = workspace:FindFirstChild(n)
		if o then o:Destroy() end
	end
	if workspace:FindFirstChildOfClass("Terrain") then workspace.Terrain:Clear() end
end

-- box(name, {sx, sy, sz}, {x, y, z}, "#hex", opts): opts.mat, .neon, .tr (transparency), .shape, .rot {rx, ry, rz} deg (Roblox axes),
-- .parent, .shadow=false, .refl
function MT.box(name, size, loc, color, o)
	o = o or {}
	local p = Instance.new(o.wedge and "WedgePart" or "Part")
	p.Name = name
	p.Anchored = true
	p.CanCollide = false
	p.CanQuery = false
	p.CanTouch = false
	p.TopSurface = Enum.SurfaceType.Smooth
	p.BottomSurface = Enum.SurfaceType.Smooth
	p.Size = Vector3.new(size[1], size[3], size[2])
	if o.shape then p.Shape = o.shape end
	p.Material = o.neon and Enum.Material.Neon or (o.mat or Enum.Material.SmoothPlastic)
	p.Color = typeof(color) == "Color3" and color or C(color)
	p.Transparency = o.tr or 0
	p.Reflectance = o.refl or 0
	if o.shadow == false then p.CastShadow = false end
	local cf = CFrame.new(V(loc[1], loc[2], loc[3]))
	if o.rot then cf = cf * CFrame.Angles(rad(o.rot[1]), rad(o.rot[2]), rad(o.rot[3])) end
	p.CFrame = cf
	p.Parent = o.parent or MT.root()
	return p
end

function MT.light(part, kind, color, brightness, range, o)
	o = o or {}
	local l = Instance.new(kind)
	l.Color = typeof(color) == "Color3" and color or C(color)
	l.Brightness = brightness
	l.Range = range
	l.Shadows = o.shadows ~= false
	if kind ~= "PointLight" then l.Face = o.face or Enum.NormalId.Bottom; l.Angle = o.angle or 120 end
	l.Parent = part
	return l
end

-- sign(name, lines, {x,y,z}, w, h, opts): a board facing the camera side (-Y in shot coords) with text lines
function MT.sign(name, lines, loc, w, h, o)
	o = o or {}
	local board = MT.box(name, { w, 0.2, h }, loc, o.bg or "#FFFDF6", { rot = o.rot })
	if o.border then
		local b = MT.box(name .. "_b", { w + 0.35, 0.16, h + 0.35 }, { loc[1], loc[2] + 0.06, loc[3] }, o.border, { rot = o.rot })
		b.CFrame = board.CFrame * CFrame.new(0, 0, -0.06)
	end
	local g = Instance.new("SurfaceGui")
	g.Face = Enum.NormalId.Back
	g.SizingMode = Enum.SurfaceGuiSizingMode.PixelsPerStud
	g.PixelsPerStud = 120
	g.LightInfluence = 1
	g.Parent = board
	local n = #lines
	local total = 0
	local sizes = o.sizes or {}
	for i = 1, n do sizes[i] = sizes[i] or (1 / n * 0.8); total += sizes[i] end
	local y = (1 - total * 1.15) / 2
	for i, txt in ipairs(lines) do
		local t = Instance.new("TextLabel")
		t.BackgroundTransparency = 1
		t.Size = UDim2.fromScale(0.94, sizes[i])
		t.Position = UDim2.fromScale(0.03, y)
		y += sizes[i] * 1.15
		t.Text = txt
		t.TextScaled = true
		t.Font = Enum.Font.GothamBold
		pcall(function() t.FontFace = Font.new("rbxasset://fonts/families/GothamSSm.json", i == 1 and Enum.FontWeight.Heavy or Enum.FontWeight.Bold) end)
		t.TextColor3 = C((o.colors and o.colors[i]) or "#3A3F4A")
		t.Parent = g
	end
	return board
end

-------------------------------------------------------------------------------------------------- characters
local SKIN = "#E8B98F"
MT.POSES = {
	rest = {}, wave = { arm_R = { 0, 0, 150 } }, hands_up = { arm_L = { 0, 0, 150 }, arm_R = { 0, 0, 150 } },
	arms_out = { arm_L = { 0, 0, 75 }, arm_R = { 0, 0, 75 } }, point = { arm_R = { 85, 0, 0 } },
	reach = { arm_L = { 80, 0, 10 }, arm_R = { 80, 0, 10 } }, shrug = { arm_L = { 0, 0, 30 }, arm_R = { 0, 0, 30 }, head = { 0, 0, 8 } },
	hug_self = { arm_L = { 75, 5, 0 }, arm_R = { 75, 5, 0 }, head = { 10, 0, 0 } },      -- R6 arms can't cross the chest without going through it
	cover_face = { arm_L = { 110, 5, 20 }, arm_R = { 110, 5, 20 }, head = { 12, 0, 0 } },
	sad = { head = { 22, 0, 0 }, torso = { 6, 0, 0 } },
	run_ready = { arm_L = { -35, 0, 8 }, arm_R = { 45, 0, 8 }, torso = { 12, 0, 0 } },
}

local function hairParts(style, col, head, parent)
	local parts = {}
	local function add(size, off, shape, c)
		local p = Instance.new("Part")
		p.Anchored = true; p.CanCollide = false; p.CanQuery = false
		p.Material = Enum.Material.SmoothPlastic
		p.TopSurface = Enum.SurfaceType.Smooth; p.BottomSurface = Enum.SurfaceType.Smooth
		p.Color = c or col
		p.Size = size
		if shape then p.Shape = shape end
		p.Parent = parent
		table.insert(parts, { p, off })
	end
	local B = Enum.PartType.Ball
	if style == "fluffy" then
		local rnd = Random.new(7)
		for i = 1, 22 do
			local a = i / 22 * math.pi * 2
			local ring = i % 2 == 0
			local r = ring and 0.78 or 0.42
			local y = ring and 0.62 or 1.0
			local s = rnd:NextNumber(0.74, 1.0)
			add(Vector3.new(s, s, s), CFrame.new(math.cos(a) * r, y + rnd:NextNumber(-0.06, 0.1), math.sin(a) * r * 0.92 + 0.02), B)
		end
		add(Vector3.new(1.05, 0.95, 1.05), CFrame.new(0, 1.12, 0.0), B)
		add(Vector3.new(1.6, 0.9, 0.9), CFrame.new(0, 0.42, 0.62), nil)
	elseif style == "spiky" then
		add(Vector3.new(1.82, 0.42, 1.72), CFrame.new(0, 0.86, 0.02))
		for i = -2, 2 do
			add(Vector3.new(0.34, 0.75, 1.3), CFrame.new(i * 0.36, 1.25, 0.05) * CFrame.Angles(rad(-14), 0, rad(-i * 7)))
		end
		add(Vector3.new(1.82, 0.9, 0.3), CFrame.new(0, 0.35, 0.74))
	elseif style == "long" then
		add(Vector3.new(1.86, 0.5, 1.76), CFrame.new(0, 0.86, 0.02))
		add(Vector3.new(1.86, 2.3, 0.42), CFrame.new(0, -0.2, 0.76))
		add(Vector3.new(0.3, 1.9, 1.3), CFrame.new(-0.86, -0.05, 0.2))
		add(Vector3.new(0.3, 1.9, 1.3), CFrame.new(0.86, -0.05, 0.2))
		for i = -2, 2 do add(Vector3.new(0.36, 0.42, 0.22), CFrame.new(i * 0.36, 0.52, -0.82) * CFrame.Angles(0, 0, rad(i * 3))) end
	elseif style == "bob" then
		add(Vector3.new(1.9, 0.55, 1.8), CFrame.new(0, 0.86, 0.02))
		add(Vector3.new(1.9, 1.5, 0.42), CFrame.new(0, 0.1, 0.76))
		add(Vector3.new(0.34, 1.35, 1.45), CFrame.new(-0.88, 0.12, 0.12))
		add(Vector3.new(0.34, 1.35, 1.45), CFrame.new(0.88, 0.12, 0.12))
		add(Vector3.new(1.3, 0.4, 0.24), CFrame.new(-0.2, 0.55, -0.82) * CFrame.Angles(0, 0, rad(-6)))
	elseif style == "block" then
		add(Vector3.new(1.84, 0.5, 1.74), CFrame.new(0, 0.86, 0.02))
		add(Vector3.new(1.84, 0.85, 0.36), CFrame.new(0, 0.38, 0.74))
		add(Vector3.new(1.5, 0.34, 0.5), CFrame.new(0.12, 1.08, -0.52) * CFrame.Angles(rad(10), 0, rad(-5)))
	end
	return parts
end

-- who(name, style, {x,y,z}, facingDeg): style = {skin, shirt, pants, shoes, hair, hair_style, scale}
function MT.make(name, st, at, facing)
	local m = Instance.new("Model")
	m.Name = name
	m.Parent = MT.root()
	local s = st.scale or 1
	local function part(n, size, color)
		local p = Instance.new("Part")
		p.Name = n; p.Anchored = true; p.CanCollide = false; p.CanQuery = false
		p.Material = Enum.Material.SmoothPlastic
		p.TopSurface = Enum.SurfaceType.Smooth; p.BottomSurface = Enum.SurfaceType.Smooth
		p.Size = size * s
		p.Color = C(color)
		p.Parent = m
		return p
	end
	local skin = st.skin or SKIN
	local rig = { name = name, model = m, scale = s, st = st, pose = {}, lift = 0, lie = nil }
	rig.torso = part("Torso", Vector3.new(2, 2, 1), st.shirt)
	rig.head = part("Head", Vector3.new(2, 1, 1) * (MT.HEAD or 1.25), skin)
	local hm = Instance.new("SpecialMesh"); hm.MeshType = Enum.MeshType.Head; hm.Scale = Vector3.new(1.25, 1.25, 1.25); hm.Parent = rig.head
	rig.armL = part("ArmL", Vector3.new(0.95, 2, 0.95), st.sleeves and st.shirt or skin)
	rig.armR = part("ArmR", Vector3.new(0.95, 2, 0.95), st.sleeves and st.shirt or skin)
	rig.slvL = part("SleeveL", Vector3.new(1.0, 0.85, 1.0), st.shirt)
	rig.slvR = part("SleeveR", Vector3.new(1.0, 0.85, 1.0), st.shirt)
	rig.legL = part("LegL", Vector3.new(0.98, 2, 0.98), st.pants)
	rig.legR = part("LegR", Vector3.new(0.98, 2, 0.98), st.pants)
	rig.shoeL = part("ShoeL", Vector3.new(1.04, 0.45, 1.12), st.shoes or "#F4F4F0")
	rig.shoeR = part("ShoeR", Vector3.new(1.04, 0.45, 1.12), st.shoes or "#F4F4F0")
	local d = Instance.new("Decal")
	d.Name = "Face"; d.Face = Enum.NormalId.Front
	d.Parent = rig.head
	rig.face = d
	rig.hair = hairParts(st.hair_style or "block", C(st.hair or "#2A1E18"), rig.head, m)
	for _, hp in ipairs(rig.hair) do hp[1].Size = hp[1].Size * s * 1.16 end
	rig.pos = V(at[1], at[2], at[3] or 0)
	rig.facing = facing or 0
	rig.extra = {}       -- props glued to a body part: {part, "armR", CFrame offset}
	MT.rigs[name] = rig
	MT.setFace(name, "neutral")
	MT.apply(name)
	return rig
end

function MT.setFace(name, face)
	local rig = MT.rigs[name]
	rig.faceName = face
	rig.face.Texture = MT.FACES[face] or MT.FACES.neutral or ""
end

local function ang(t) t = t or { 0, 0, 0 }; return t[1] or 0, t[2] or 0, t[3] or 0 end

-- recompute every part of a rig from rig.pos / rig.facing / rig.pose / rig.lift / rig.lie
function MT.apply(name)
	local rig = MT.rigs[name]
	local s = rig.scale
	local a = rad(rig.facing)
	local fwd = Vector3.new(math.sin(a), 0, math.cos(a))
	local root = CFrame.lookAt(rig.pos + Vector3.new(0, rig.lift, 0), rig.pos + Vector3.new(0, rig.lift, 0) + fwd)
	if rig.lie == "down" then root = root * CFrame.Angles(rad(-90), 0, 0)
	elseif rig.lie == "up" then root = root * CFrame.Angles(rad(90), 0, 0) end
	local P = rig.pose
	local tp, ty, tr = ang(P.torso)
	local hip = root * CFrame.new(0, 2 * s, 0) * CFrame.Angles(rad(-tp), rad(ty), rad(-tr))
	rig.torso.CFrame = hip * CFrame.new(0, 1 * s, 0)
	local hp, hy, hr = ang(P.head)
	local neck = hip * CFrame.new(0, 2 * s, 0) * CFrame.Angles(rad(-hp), rad(-hy), rad(hr))
	rig.head.CFrame = neck * CFrame.new(0, 0.5 * (MT.HEAD or 1.25) * s, 0)
	for _, h in ipairs(rig.hair) do h[1].CFrame = rig.head.CFrame * CFrame.new(h[2].Position * s * 1.16) * h[2].Rotation end
	for side, sgn in pairs({ L = -1, R = 1 }) do
		local f, across, out = ang(P["arm_" .. side])
		local sh = hip * CFrame.new(sgn * 1.48 * s, 1.75 * s, 0) * CFrame.Angles(0, rad(sgn * across), 0) * CFrame.Angles(rad(f), 0, rad(sgn * out))
		rig["arm" .. side].CFrame = sh * CFrame.new(0, -0.75 * s, 0)
		rig["slv" .. side].CFrame = sh * CFrame.new(0, -0.18 * s, 0)
		local lf, _, lo = ang(P["leg_" .. side])
		local hj = root * CFrame.new(sgn * 0.5 * s, 2 * s, 0) * CFrame.Angles(rad(lf), 0, rad(sgn * lo))
		rig["leg" .. side].CFrame = hj * CFrame.new(0, -1 * s, 0)
		rig["shoe" .. side].CFrame = hj * CFrame.new(0, -1.8 * s, -0.07 * s)
	end
	for _, e in ipairs(rig.extra) do e[1].CFrame = rig[e[2]].CFrame * e[3] end
end

function MT.set(name, t)        -- t = {pos=, facing=, pose=, lift=, lie=, face=}
	local rig = MT.rigs[name]
	for k, v in pairs(t) do
		if k == "face" then MT.setFace(name, v) elseif k == "pos" then rig.pos = V(v[1], v[2], v[3] or 0) else rig[k] = v end
	end
	MT.apply(name)
end

function MT.headPos(name) return MT.rigs[name].head.Position end

-------------------------------------------------------------------------------------------------- camera
-- portrait trick: the camera is rolled 90 degrees so the tall frame fills the wide Studio viewport; ffmpeg rotates it back.
function MT.cam(loc, look, fovH, roll)
	local cam = workspace.CurrentCamera
	cam.CameraType = Enum.CameraType.Scriptable
	local p, l = V(loc[1], loc[2], loc[3]), V(look[1], look[2], look[3])
	cam.CFrame = CFrame.lookAt(p, l) * CFrame.Angles(0, 0, rad(roll or 90))
	cam.FieldOfView = fovH
	cam.Focus = CFrame.new(l)
	MT.camState = { p = p, l = l, fov = fovH }
end

-- lens (mm, Blender 36 mm sensor on the tall side) -> FieldOfView for the rolled camera (= horizontal FOV of the portrait frame)
function MT.lensFov(lens) return math.deg(2 * math.atan((36 * 9 / 16) / 2 / lens)) end

return "MT lib loaded"
