-- MT part 2: looks (lighting), sets, cast, crowd, frame engine
local MT = shared.MT
local Lighting = game:GetService("Lighting")
local rad, V, C = math.rad, MT.V, MT.C
local RGB = Color3.fromRGB

local function ensure(class, name, parent)
	local i = parent:FindFirstChild(name)
	if i and not i:IsA(class) then i:Destroy(); i = nil end
	if not i then i = Instance.new(class); i.Name = name; i.Parent = parent end
	return i
end

local SUN_CACHE = {}
function MT.sun(dx, dy, dz)          -- direction from the scene toward the sun, shot coords (z up)
	local key = string.format("%.2f,%.2f,%.2f", dx, dy, dz)
	local want = V(dx, dy, dz).Unit
	local best = SUN_CACHE[key]
	if not best then
		local bd = -2
		for lat = -85, 85, 5 do
			Lighting.GeographicLatitude = lat
			for ct = 6.5, 17.5, 0.25 do
				Lighting.ClockTime = ct
				local d = Lighting:GetSunDirection():Dot(want)
				if d > bd then bd = d; best = { ct, lat } end
			end
		end
		SUN_CACHE[key] = best
	end
	Lighting.ClockTime = best[1]; Lighting.GeographicLatitude = best[2]
end

MT.LOOKS = {
	day = { b = 2.7, exp = 0.12, amb = RGB(128, 126, 134), out = RGB(156, 158, 168), soft = 0.5, top = RGB(255, 244, 226),
		atmo = { 0.24, 0.05, RGB(214, 229, 243), RGB(150, 176, 206), 0, 0.8 }, bloom = { 0.28, 28, 1.25 },
		cc = { 0.015, 0.06, 0.14, RGB(255, 251, 245) }, rays = 0.035 },
	warm = { b = 2.4, exp = 0.1, amb = RGB(150, 136, 120), out = RGB(170, 156, 140), soft = 0.6, top = RGB(255, 232, 200),
		atmo = { 0.2, 0, RGB(255, 236, 205), RGB(240, 190, 140), 0, 0.5 }, bloom = { 0.35, 30, 1.15 },
		cc = { 0.02, 0.04, 0.1, RGB(255, 244, 228) }, rays = 0.02 },
	cool = { b = 2.3, exp = 0.1, amb = RGB(130, 140, 160), out = RGB(150, 165, 190), soft = 0.7, top = RGB(225, 238, 255),
		atmo = { 0.34, 0.1, RGB(200, 220, 240), RGB(150, 175, 215), 0, 1.4 }, bloom = { 0.45, 36, 1.05 },
		cc = { 0.02, -0.02, -0.12, RGB(232, 240, 255) }, rays = 0.06 },
	night = { night = true, b = 1.6, exp = 0.35, amb = RGB(64, 78, 128), out = RGB(84, 100, 158), soft = 0.4, top = RGB(190, 205, 255),
		atmo = { 0.3, 0.2, RGB(70, 88, 140), RGB(40, 50, 90), 0, 1.2 }, bloom = { 0.6, 34, 0.95 },
		cc = { 0.0, 0.05, 0.02, RGB(214, 224, 255) }, rays = 0 },
}

function MT.look(name, sun)
	local k = MT.LOOKS[name]
	pcall(function() Lighting.LightingStyle = Enum.LightingStyle.Realistic end)
	pcall(function() Lighting.PrioritizeLightingQuality = true end)
	Lighting.GlobalShadows = true
	Lighting.Brightness = k.b; Lighting.ExposureCompensation = k.exp
	Lighting.Ambient = k.amb; Lighting.OutdoorAmbient = k.out
	Lighting.ShadowSoftness = k.soft; Lighting.ColorShift_Top = k.top
	Lighting.EnvironmentDiffuseScale = 1; Lighting.EnvironmentSpecularScale = 0.3
	if k.night then Lighting.GeographicLatitude = 35; Lighting.ClockTime = 0.4
	else sun = sun or { -0.5, -0.62, 0.62 }; MT.sun(sun[1], sun[2], sun[3]) end
	local a = ensure("Atmosphere", "Atmosphere", Lighting)
	a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = k.atmo[1], k.atmo[2], k.atmo[3], k.atmo[4], k.atmo[5], k.atmo[6]
	local b = ensure("BloomEffect", "Bloom", Lighting); b.Enabled = true
	b.Intensity, b.Size, b.Threshold = k.bloom[1], k.bloom[2], k.bloom[3]
	local cc = ensure("ColorCorrectionEffect", "MTColor", Lighting); cc.Enabled = true
	cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = k.cc[1], k.cc[2], k.cc[3], k.cc[4]
	local r = ensure("SunRaysEffect", "SunRays", Lighting); r.Enabled = k.rays > 0; r.Intensity = k.rays; r.Spread = 0.4
	local d = Lighting:FindFirstChild("DepthOfField"); if d then d.Enabled = false end
	local cl = ensure("Clouds", "Clouds", workspace.Terrain)
	cl.Cover = k.night and 0.35 or 0.52; cl.Density = 0.62; cl.Color = k.night and RGB(120, 135, 190) or RGB(255, 255, 255)
	MT.lookName = name
end

-------------------------------------------------------------------------------------------------- cast
local P = { butter = "#F5D66E", teal = "#45B5AA", lilac = "#B7A3E6", navy = "#2F3E63", pink = "#F6A6C1", mint = "#A8E0C0", coral = "#EE6F5E",
	sky = "#8FC9F0", white = "#FAFAF7", wood = "#B98A5E", deep_teal = "#2C7A78", cream = "#FBF1DC", charcoal = "#3A3F4A", light_wood = "#E3C598" }
MT.P = P
MT.CAST = {
	me = { skin = "#E8B98F", shirt = P.butter, pants = "#3D4A6B", shoes = "#F4F4F0", hair = "#2A1E18", hair_style = "fluffy" },
	diddy = { skin = "#C98F65", shirt = P.teal, pants = "#2E3138", shoes = "#F4F4F0", hair = "#17141A", hair_style = "spiky" },
	mom = { skin = "#E8B98F", shirt = P.lilac, pants = "#5A4A7A", shoes = "#FAFAF7", hair = "#4A3020", hair_style = "long" },
	dad = { skin = "#DDAA80", shirt = P.navy, pants = "#2B2B33", shoes = "#1A1A1E", hair = "#2A1E18", hair_style = "block" },
	may = { skin = "#F1C9A5", shirt = P.pink, pants = "#FAFAF7", shoes = "#EE6F5E", hair = "#E9A23B", hair_style = "bob" },
	mayor = { skin = "#E3B58D", shirt = "#3A3F4A", pants = "#3A3F4A", shoes = "#1A1A1E", hair = "#D9D9D9", hair_style = "none", sleeves = true },
	teacher = { skin = "#D9A57E", shirt = P.mint, pants = "#6B5B4A", shoes = "#4A3020", hair = "#8A8A8A", hair_style = "bob" },
	thing = { skin = "#DCE6F2", shirt = "#DCE6F2", pants = "#DCE6F2", shoes = "#DCE6F2", hair = "#DCE6F2", hair_style = "none", sleeves = true },
}
MT.CAST.boy = MT.CAST.me
local SKINS = { "#F1C9A5", "#E8B98F", "#D9A57E", "#C98F65", "#A8714D", "#8A5A3C" }
local SHIRTS = { P.coral, P.sky, P.mint, P.pink, P.white, P.wood, P.deep_teal, "#E88FB0", "#8FC1E8", "#F2B66B" }
local PANTS = { "#3D4A6B", "#2E3138", "#6B5B4A", "#5A4A7A", "#4A5A4A" }
local HAIRS = { "#2A1E18", "#17141A", "#4A3020", "#7A4A28", "#C9A25A", "#8A8A8A" }
local STYLES = { "block", "fluffy", "long", "bob", "spiky" }
local function styleOf(base)
	if MT.CAST[base] then return MT.CAST[base] end
	local r = Random.new(tonumber(base:sub(2)) * 7 + 3)
	return { skin = SKINS[r:NextInteger(1, 6)], shirt = SHIRTS[r:NextInteger(1, 10)], pants = PANTS[r:NextInteger(1, 5)], shoes = "#F4F4F0",
		hair = HAIRS[r:NextInteger(1, 6)], hair_style = STYLES[r:NextInteger(1, 5)] }
end
local function faceTo(p, t) return math.deg(math.atan2(t[1] - p[1], -(t[2] - p[2]))) end
MT.faceTo = faceTo

-- who(name, {x,y,z}, opts): opts.facing, .look={x,y}, .face, .pose (name), .bones (table), .scale, .lie
function MT.who(name, at, o)
	o = o or {}
	local base = name:match("^[^#]+")
	local st = table.clone(styleOf(base)); st.scale = o.scale
	local facing = o.look and faceTo(at, o.look) or (o.facing or 0)
	local rig = MT.make(name, st, at, facing)
	local pose = {}
	if o.pose then for k, v in pairs(MT.POSES[o.pose]) do pose[k] = v end end
	if o.bones then for k, v in pairs(o.bones) do pose[k] = v end end
	rig.pose = pose; rig.lie = o.lie; rig.poseName = o.pose; rig.hold = o.hold
	MT.setFace(name, o.face or "neutral")
	MT.apply(name)
	return rig
end

function MT.near(name, dx, dy, dz)    -- point in a character's own frame (shot coords): dx to its left, dy in front, dz up
	local rig = MT.rigs[name]
	local a = rad(rig.facing)
	local p = rig.pos
	local x, y, z = p.X, -p.Z, p.Y
	local s = rig.scale
	return { x + (math.cos(a) * dx + math.sin(a) * dy) * s, y + (math.sin(a) * dx - math.cos(a) * dy) * s, z + dz * s }
end

-------------------------------------------------------------------------------------------------- props and sets
function MT.rock(name, loc, s)
	s = s or 1
	return MT.box(name, { 0.95 * s, 0.8 * s, 0.7 * s }, loc, "#9AA3AD", { mat = Enum.Material.Slate, rot = { 12, 25, 8 } })
end

local LAMPC = { off = "#E9E9DD", white = "#FFFFFF", green = "#3FD27A", red = "#F2463C" }
function MT.lamp(color, at)
	at = at or { 2.9, 8.5, 1.2 }
	local x, y, z = at[1], at[2], at[3]
	local body = "#2C7A78"
	for i, d in ipairs({ { 0.55, 0.45 }, { 0.55, -0.45 }, { -0.5, 0 } }) do
		MT.box("lamp_leg" .. i, { 0.16, 0.16, 3.0 }, { x + d[1], y + d[2], z + 1.5 }, body, { rot = { d[2] * 14, 0, -d[1] * 10 } })
	end
	MT.box("lamp_pole", { 0.24, 0.24, 1.4 }, { x, y, z + 3.5 }, body)
	MT.box("lamp_head", { 1.5, 1.5, 1.5 }, { x + 0.1, y, z + 4.7 }, body)
	MT.box("lamp_rim", { 0.3, 1.7, 1.7 }, { x - 0.62, y, z + 4.7 }, "#1F5957", { shape = Enum.PartType.Cylinder })
	local on = color ~= "off"
	local lens = MT.box("lamp_lens", { 0.22, 1.25, 1.25 }, { x - 0.74, y, z + 4.7 }, LAMPC[color], { neon = on, shape = Enum.PartType.Cylinder })
	local tell = MT.box("lamp_tell", { 1.0, 0.14, 0.4 }, { x + 0.1, y - 0.78, z + 5.1 }, LAMPC[color], { neon = on })
	MT.lampParts = { lens = lens, tell = tell, on = on, color = LAMPC[color] }
	if on then
		local holder = MT.box("lamp_glow", { 0.2, 0.2, 0.2 }, { x - 0.9, y, z + 4.7 }, "#000000", { tr = 1, shadow = false })
		holder.CFrame = CFrame.lookAt(holder.Position, V(x - 6, y, z + 4.4))
		local sl = MT.light(holder, "SpotLight", LAMPC[color], color == "white" and 6 or 9, 22, { face = Enum.NormalId.Front, angle = 70 })
		local pl = MT.light(holder, "PointLight", LAMPC[color], color == "white" and 1.2 or 2.2, 12, { shadows = false })
		MT.lampParts.lights = { { sl, sl.Brightness }, { pl, pl.Brightness } }
	end
end

function MT.house(name, x, y, body, roof, o)
	o = o or {}
	local w, h, d = o.w or 7, o.h or 5.5, o.d or 6
	MT.box(name, { w, d, h }, { x, y, h / 2 }, body)
	local rh = w * 0.42
	for sgn = -1, 1, 2 do     -- gable roof from two wedges, ridge runs front to back
		local wd = Instance.new("WedgePart")
		wd.Anchored = true; wd.CanCollide = false; wd.Material = Enum.Material.SmoothPlastic; wd.Color = C(roof)
		wd.Size = Vector3.new(d + 0.9, rh, w / 2 + 0.45)
		wd.CFrame = CFrame.new(V(x + sgn * (w / 4 + 0.22), y, h + rh / 2)) * CFrame.Angles(0, rad(sgn * 90), 0)
		wd.Parent = MT.root()
	end
	local fy = y + (d / 2 + 0.05) * (o.flip and 1 or -1)
	MT.box(name .. "_door", { 1.5, 0.16, 2.8 }, { x - w * 0.2, fy, 1.4 }, "#B98A5E")
	MT.box(name .. "_knob", { 0.2, 0.26, 0.2 }, { x - w * 0.2 + 0.45, fy, 1.4 }, "#F5D66E", { shape = Enum.PartType.Ball })
	MT.box(name .. "_winf", { 2.0, 0.14, 2.0 }, { x + w * 0.2, fy, 3.4 }, "#FAFAF7")
	local g = MT.box(name .. "_wing", { 1.55, 0.2, 1.55 }, { x + w * 0.2, fy, 3.4 }, o.lit and "#FFE9A8" or "#BFE3F7", { neon = o.lit, refl = o.lit and 0 or 0.25 })
	MT.box(name .. "_wbar", { 0.12, 0.24, 1.55 }, { x + w * 0.2, fy, 3.4 }, "#FAFAF7")
	MT.box(name .. "_sill", { 2.3, 0.5, 0.18 }, { x + w * 0.2, fy, 2.3 }, "#FAFAF7")
	if o.lit then MT.light(g, "PointLight", "#FFDFA0", 1.4, 14, { shadows = false }) end
	return fy
end

function MT.tree(name, x, y, s, dark)
	s = s or 1
	MT.box(name .. "_t", { 0.9 * s, 0.9 * s, 3.0 * s }, { x, y, 1.5 * s }, "#8A5E3C", { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
	local greens = dark and { "#3E6B55", "#35604B", "#2C5341" } or { "#7CC08E", "#69B37E", "#8FCC9E" }
	local r = Random.new(math.floor(x * 13 + y * 7))
	for i = 1, 7 do
		local a = i / 6 * math.pi * 2
		local rr = i == 7 and 0 or 1.25 * s
		local sz = (i == 7 and 3.6 or r:NextNumber(2.4, 3.1)) * s
		MT.box(name .. "_f" .. i, { sz, sz, sz }, { x + math.cos(a) * rr, y + math.sin(a) * rr, (i == 7 and 5.6 or r:NextNumber(3.9, 4.8)) * s }, greens[i % 3 + 1],
			{ shape = Enum.PartType.Ball })
	end
end

function MT.ground(a, b, tile, mat)
	MT.box("ground", { 600, 600, 2 }, { 0, 0, -1 }, a, { mat = mat })
	if b then
		local n = 14
		for i = -n, n do for j = -n, n do
			if (i + j) % 2 == 0 then MT.box("tile", { tile, tile, 0.06 }, { i * tile, j * tile, 0.02 }, b, { shadow = false, mat = mat }) end
		end end
	end
end

local HOUSE_COLS = { { P.cream, P.coral }, { P.mint, P.deep_teal }, { P.pink, P.navy }, { P.butter, P.wood }, { "#CFE6F7", P.navy }, { P.lilac, "#5A4A7A" } }
function MT.town()
	MT.ground("#EFE3CB", "#E6D5B5", 3.0)
	MT.box("lawn_b", { 600, 240, 0.1 }, { 0, 140, 0.03 }, "#BFE3B0", { mat = Enum.Material.Grass })
	MT.box("lawn_f", { 600, 240, 0.1 }, { 0, -146, 0.03 }, "#BFE3B0", { mat = Enum.Material.Grass })
	local i = 0
	for x = -40, 40, 10 do
		local c1, c2 = HOUSE_COLS[i % 6 + 1], HOUSE_COLS[(i + 3) % 6 + 1]
		MT.house("hb" .. i, x, 27, c1[1], c1[2])
		MT.house("hf" .. i, x + 5, -32, c2[1], c2[2], { flip = true })
		i += 1
	end
	for k, p in ipairs({ { -14, 20 }, { 14, 20 }, { -24, 16 }, { 24, 16 }, { -18, -24 }, { 17, -25 }, { -30, -20 }, { 30, -22 } }) do
		MT.tree("tr" .. k, p[1], p[2], 1.15)
	end
end

function MT.setSquare(lampCol, o)
	o = o or {}
	MT.town()
	MT.box("stage", { 18, 7, 1.2 }, { 0, 9, 0.6 }, P.light_wood, { mat = Enum.Material.WoodPlanks })
	MT.box("stage_trim", { 18.2, 0.2, 0.3 }, { 0, 5.45, 1.1 }, P.coral)
	MT.box("stage_step", { 5, 1.2, 0.6 }, { 0, 5.0, 0.3 }, P.light_wood, { mat = Enum.Material.WoodPlanks })
	MT.box("backdrop", { 18, 0.5, 8.5 }, { 0, 12.6, 5.4 }, P.cream)
	MT.box("backdrop_band", { 18, 0.12, 0.7 }, { 0, 12.3, 3.0 }, P.teal)
	MT.box("post_l", { 0.5, 0.5, 9.4 }, { -9.2, 12.4, 4.7 }, P.deep_teal)
	MT.box("post_r", { 0.5, 0.5, 9.4 }, { 9.2, 12.4, 4.7 }, P.deep_teal)
	MT.sign("banner", { "TEST DAY", "happy 18th!" }, { 0, 12.25, 7.6 }, 9.5, 2.6, { border = P.coral, colors = { P.charcoal, P.coral }, sizes = { 0.5, 0.26 } })
	local flag = { P.coral, P.butter, P.teal, P.pink, P.sky, P.lilac }
	for i = 0, 17 do     -- bunting across the top of the stage
		MT.box("flag" .. i, { 0.7, 0.06, 0.8 }, { -8.5 + i, 12.1, 9.75 - math.abs(math.sin(i / 17 * math.pi)) * 0.5 }, flag[i % 6 + 1], { rot = { 0, 0, 45 } })
	end
	MT.lamp(lampCol or "off")
	if o.reverse then MT.look(o.look or "day", { 0.5, 0.62, 0.62 }) else MT.look(o.look or "day") end
end

MT.CROWD = {}
for r = 0, 3 do for _, x in ipairs({ -15.4, -11.0, -6.6, -2.2, 2.2, 6.6, 11.0, 15.4 }) do
	table.insert(MT.CROWD, { x + (r % 2 == 1 and 1.1 or -0.6), 1.8 - r * 3.3 })
end end

function MT.crowd(n, o)
	o = o or {}
	local skip = {}
	for _, i in ipairs(o.skip or {}) do skip[i] = true end
	local nskip = #(o.skip or {})
	local j = 0
	for i = 0, math.min(#MT.CROWD, n + nskip) - 1 do
		if not skip[i] then
			local p = MT.CROWD[i + 1]
			local f = o.faces and o.faces[j % #o.faces + 1] or (o.face or "neutral")
			local name = "x" .. ((o.start or 0) + i)
			local hold = o.rocks and j % 2 == 0
			MT.who(name, p, { look = o.look or { 0, 8.5 }, face = f, pose = o.pose, hold = hold })
			if hold then
				local rk = MT.rock("rock" .. i, { 0, 0, 0 }, 0.9)
				table.insert(MT.rigs[name].extra, { rk, "armR", CFrame.new(0, -1.35, 0) })
				MT.apply(name)
			end
			j += 1
		end
	end
end

function MT.mayor(o)
	o = o or {}
	local at = o.at or { 4.5, 10.3, 1.2 }
	local rig = MT.who("mayor", at, { look = o.look or { 0, 8.5 }, face = o.face or "stare", pose = o.pose, bones = o.bones })
	local function hat(n, size, off, col, shape)
		local p = MT.box(n, { 1, 1, 1 }, { 0, 0, 0 }, col, { shape = shape, parent = rig.model })
		p.Size = size
		table.insert(rig.extra, { p, "head", off })
	end
	hat("hat_brim", Vector3.new(0.16, 2.5, 2.5), CFrame.new(0, 0.6 * MT.HEAD + 0.06, 0) * CFrame.Angles(0, 0, rad(90)), "#2E3138", Enum.PartType.Cylinder)
	hat("hat_top", Vector3.new(1.2, 1.6, 1.6), CFrame.new(0, 0.6 * MT.HEAD + 0.69, 0) * CFrame.Angles(0, 0, rad(90)), "#2E3138", Enum.PartType.Cylinder)
	hat("hat_band", Vector3.new(0.3, 1.66, 1.66), CFrame.new(0, 0.6 * MT.HEAD + 0.26, 0) * CFrame.Angles(0, 0, rad(90)), P.coral, Enum.PartType.Cylinder)
	MT.apply("mayor")
	return rig
end

-------------------------------------------------------------------------------------------------- frame engine
MT.SHOTS = MT.SHOTS or {}
local BLINKY = { neutral = 1, smile = 1, happy = 1, content = 1, sad = 1, nervous = 1, oh = 1, sleepy = 1, nerd = 1, angry = 1, smirk = 1 }
local STILL = { stare = 1, creepy = 1 }
local PUMP = { wave = 1, hands_up = 1 }

local function copyPose(p) local t = {}; for k, v in pairs(p) do t[k] = { v[1], v[2], v[3] } end; return t end
local function addA(t, k, d) local v = t[k] or { 0, 0, 0 }; t[k] = { v[1] + d[1], v[2] + d[2], v[3] + d[3] } end
MT.addA = addA
local function ease(p) p = math.clamp(p, 0, 1); return 0.5 - 0.5 * math.cos(p * math.pi) end
MT.ease = ease

function MT.build(id)
	MT.clear()
	MT.lampParts = nil
	local def = MT.SHOTS[id]
	MT.camBase = def.build()
	local i = 0
	local names = {}
	for name in pairs(MT.rigs) do table.insert(names, name) end
	table.sort(names)
	for _, name in ipairs(names) do
		local rig = MT.rigs[name]
		i += 1
		rig.seed = i * 1.37 + (def.idx or 0) * 0.61
		rig.base = { pos = rig.pos, facing = rig.facing, pose = copyPose(rig.pose), face = rig.faceName, scale = rig.scale }
	end
	MT.cur = id
end

function MT.frame(id, f)
	if MT.cur ~= id then MT.build(id) end
	local def = MT.SHOTS[id]
	local n = def.n or 30
	local t = (f - 1) / 30
	for name, rig in pairs(MT.rigs) do
		local b = rig.base
		rig.pos, rig.facing, rig.lift = b.pos, b.facing, 0
		local pose = copyPose(b.pose)
		rig.pose = pose
		local face = b.face
		local skip = def.skip and def.skip[name]
		if not rig.lie and not skip then
			local s = rig.seed
			local still = STILL[b.face] and 0.5 or 1
			addA(pose, "torso", { 1.3 * math.sin(t * 4.2 + s), 0, 0 })
			if def.speak ~= name then
				addA(pose, "head", { 2.6 * still * math.sin(t * 2.1 + s * 2), 3.6 * still * math.sin(t * 1.3 + s * 3), 3.2 * still * math.sin(t * 1.7 + s * 5) })
			end
			local raised = false
			for _, k in ipairs({ "arm_L", "arm_R" }) do if (b.pose[k] and b.pose[k][1] or 0) >= 60 then raised = true end end
			if PUMP[rig.poseName or ""] and not rig.hold and not (def.noarms and def.noarms[name]) then
				local w = 16 * math.sin(t * 13 + s)
				addA(pose, "arm_L", { 0, 0, w }); addA(pose, "arm_R", { 0, 0, -w })
			elseif not raised and not rig.hold and not (def.noarms and def.noarms[name]) then
				local w = 2.5 + 2.5 * math.sin(t * 4.2 + s)
				addA(pose, "arm_L", { 0, 0, w }); addA(pose, "arm_R", { 0, 0, w })
			end
			if def.speak == name then
				face = (math.floor((f + s) / 4) % 2 == 0) and "talk" or b.face
				addA(pose, "head", { 4 * math.sin(t * 9 + s), 2 * math.sin(t * 5), 3 * math.sin(t * 7 + s) })
			elseif BLINKY[b.face] and n >= 20 then
				local fb = 6 + math.floor((s * 7919) % math.max(1, n - 14))
				if f >= fb and f < fb + 3 then face = "blink" end
			end
		end
		rig.wantFace = face
	end
	if def.act then def.act(f, n, t) end
	for name, rig in pairs(MT.rigs) do
		if rig.faceName ~= rig.wantFace then MT.setFace(name, rig.wantFace) end
		MT.apply(name)
	end
	if def.lampOn and MT.lampParts and MT.lampParts.on then
		local lit = f >= 4
		local lp = MT.lampParts
		for _, k in ipairs({ "lens", "tell" }) do lp[k].Material = lit and Enum.Material.Neon or Enum.Material.SmoothPlastic; lp[k].Color = lit and C(lp.color) or C("#E9E9DD") end
		for _, l in ipairs(lp.lights or {}) do l[1].Brightness = lit and l[2] or 0 end
	end
	local cb = MT.camBase
	local loc, look = V(cb[1][1], cb[1][2], cb[1][3]), V(cb[2][1], cb[2][2], cb[2][3])
	local dist = (look - loc).Magnitude
	local amt = def.creep and dist * 0.16 or dist * 0.075 * math.clamp(n / 45, 0.6, 1.4) * ((def.idx or 0) % 4 == 3 and -1 or 1)
	if cb.push then amt = cb.push end
	local p = loc + (look - loc).Unit * amt * ease((f - 1) / math.max(1, n - 1))
	local cam = workspace.CurrentCamera
	cam.CameraType = Enum.CameraType.Scriptable
	cam.CFrame = CFrame.lookAt(p, look)
	cam.FieldOfView = math.deg(2 * math.atan(18 / (cb[3] or 35)))   -- vertical FOV of the 9:16 frame (crop the middle of the viewport)
	cam.Focus = CFrame.new(look)
end

-- helpers for per-shot actions
function MT.face(name, f) MT.rigs[name].wantFace = f end
function MT.jump(name, f, at)
	local k = { { 0, 0 }, { 6, 0.7 }, { 12, 0 }, { 18, 0.4 }, { 24, 0 } }
	local x = f - at
	for i = 1, #k - 1 do
		if x >= k[i][1] and x <= k[i + 1][1] then
			local p = (x - k[i][1]) / (k[i + 1][1] - k[i][1])
			MT.rigs[name].lift = k[i][2] + (k[i + 1][2] - k[i][2]) * ease(p)
		end
	end
end
function MT.recoil(name, f, at, face)
	local rig = MT.rigs[name]
	if f < at then return end
	if face then rig.wantFace = face end
	local x = f - at
	local p = ease(math.min(1, x / 3))
	local settle = ease(math.clamp((x - 3) / 11, 0, 1))
	addA(rig.pose, "torso", { -14 * p + 8 * settle, 0, 0 })
	addA(rig.pose, "head", { -12 * p + 7 * settle, 0, 0 })
	addA(rig.pose, "arm_L", { 60 * p - 15 * settle, 0, 40 * p - 10 * settle })
	addA(rig.pose, "arm_R", { 60 * p - 15 * settle, 0, 40 * p - 10 * settle })
	rig.lift = x <= 3 and 0.25 * p or 0.25 * (1 - ease(math.clamp((x - 3) / 6, 0, 1)))
end
function MT.walk(name, f, f0, f1, from, to, run)
	local rig = MT.rigs[name]
	local p = math.clamp((f - f0) / math.max(1, f1 - f0), 0, 1)
	local x, y, z = from[1] + (to[1] - from[1]) * p, from[2] + (to[2] - from[2]) * p, (from[3] or 0) + ((to[3] or 0) - (from[3] or 0)) * p
	rig.pos = V(x, y, z)
	rig.facing = faceTo(from, to)
	local sw = run and 56 or 35
	local ph = (f - f0) / (run and 9 or 16) * math.pi
	local s = math.sin(ph) * (p > 0 and p < 1 and 1 or 0)
	rig.pose.leg_L = { sw * s, 0, 0 }; rig.pose.leg_R = { -sw * s, 0, 0 }
	rig.pose.arm_L = { -sw * 0.9 * s, 0, 0 }; rig.pose.arm_R = { sw * 0.9 * s, 0, 0 }
	rig.pose.torso = { run and 14 or 3, 0, 0 }
	rig.lift = math.abs(math.cos(ph)) * (run and 0.18 or 0.08)
end
function MT.shake(name, f, bone, amp, every)
	local r = Random.new(math.floor(f / (every or 2)) * 31 + #name)
	addA(MT.rigs[name].pose, bone, { r:NextNumber(-amp, amp), r:NextNumber(-amp, amp), 0 })
end

return "MT lib2 loaded"
