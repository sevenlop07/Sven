-- MT part 5: interior and outdoor sets (downloaded models + a few story props)
local MT = shared.MT
local P, rad = MT.P, math.rad

function MT.cu(name, o)        -- close-up camera in front of a face (Roblox rig: head centre 4.86, head about 2.2 tall)
	o = o or {}
	local d = (o.dist or 3.9) * 1.45
	local eye = 4 + 0.5 * (MT.HEAD or 1.25) + 0.08
	local c = MT.near(name, (o.side or 0) * 1.3, d, eye + (o.height or -0.2))
	local l = MT.near(name, 0, 0, eye + (o.look_z or -0.15))
	return { c, l, o.lens or 32 }
end

function MT.room(o)
	o = o or {}
	local w, d, h = o.w or 22, o.d or 14, o.h or 9
	MT.box("floor", { w, d, 0.4 }, { 0, d / 2 - 2, -0.2 }, o.floor or "#E9DCC6", { mat = o.floorMat or Enum.Material.WoodPlanks })
	MT.box("wall_back", { w, 0.4, h }, { 0, d - 2, h / 2 }, o.wall or P.cream)
	MT.box("wall_l", { 0.4, d, h }, { -w / 2, d / 2 - 2, h / 2 }, o.wall or P.cream)
	MT.box("wall_r", { 0.4, d, h }, { w / 2, d / 2 - 2, h / 2 }, o.wall or P.cream)
	if o.band then MT.box("band", { w, 0.45, 0.5 }, { 0, d - 2.2, 3.0 }, o.band) end
	MT.box("skirting", { w, 0.5, 0.45 }, { 0, d - 2.25, 0.22 }, "#FAFAF7")
	if o.ceiling ~= false then
		local c = MT.box("ceiling", { w, d, 0.3 }, { 0, d / 2 - 2, h }, "#FAFAF7")
		for i = -1, 1 do
			local lp = MT.box("panel" .. i, { 3.2, 1.6, 0.12 }, { i * 6.5, d / 2 - 1, h - 0.2 }, "#FFFBF0", { neon = true, shadow = false })
			MT.light(lp, "SurfaceLight", "#FFF2DC", o.lamp or 1.6, 16, { face = Enum.NormalId.Bottom, angle = 120 })
		end
	end
end

function MT.table(name, loc, size, top, col)
	size = size or { 9, 2.4, 0.3 }; top = top or 2.5
	MT.box(name, size, { loc[1], loc[2], top }, col or P.light_wood, { mat = Enum.Material.Wood })
	for i, d in ipairs({ { 1, 1 }, { 1, -1 }, { -1, 1 }, { -1, -1 } }) do
		MT.box(name .. "_leg" .. i, { 0.3, 0.3, top }, { loc[1] + d[1] * (size[1] / 2 - 0.5), loc[2] + d[2] * (size[2] / 2 - 0.4), top / 2 }, col or P.light_wood, { mat = Enum.Material.Wood })
	end
end

function MT.tray(name, loc, food)
	local x, y, z = loc[1], loc[2], loc[3]
	MT.box(name, { 2.0, 1.3, 0.12 }, { x, y, z }, "#A9B1BA")
	MT.box(name .. "_bowl", { 0.9, 0.5, 0.9 }, { x - 0.3, y, z + 0.25 }, "#FAFAF7", { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
	MT.box(name .. "_food", { 0.72, 0.12, 0.72 }, { x - 0.3, y, z + 0.47 }, food or "#B98A5E", { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
	MT.box(name .. "_cup", { 0.4, 0.55, 0.4 }, { x + 0.6, y, z + 0.33 }, P.sky, { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
end

function MT.setCafe()
	MT.room({ w = 26, d = 14, h = 9, wall = P.cream, floor = "#E8E4DA", floorMat = Enum.Material.Marble, band = P.coral })
	MT.sign("menu", { "LUNCH", "MYSTERY STEW", "(again)" }, { -5.5, 11.6, 6.2 }, 4.6, 2.6, { border = P.teal, colors = { P.charcoal, P.coral, "#9AA3AD" }, sizes = { 0.3, 0.26, 0.2 } })
	MT.box("window", { 6, 0.2, 3.4 }, { 6, 11.75, 5.6 }, "#BFE3F7", { refl = 0.2 })
	MT.box("window_f", { 6.4, 0.15, 3.8 }, { 6, 11.82, 5.6 }, "#FAFAF7")
	MT.table("tbl", { 0, 1.4 }, { 10, 2.4, 0.3 }, 2.5)
	MT.table("tbl2", { 0, 5.2 }, { 10, 2.0, 0.3 }, 2.5)
	MT.look("warm")
end

function MT.cafePair(dFace, mFace, right)
	MT.who("diddy", { 2.4, 3.3 }, { facing = -8, face = dFace, bones = right ~= false and { arm_R = { 70, 0, 0 } } or { arm_L = { 70, 0, 0 } } })
	MT.who("me", { -2.4, 3.3 }, { facing = 8, face = mFace, bones = { arm_L = { 70, 0, 0 } } })
	MT.tray("tray_d", { 2.4, 1.4, 2.72 }); MT.tray("tray_m", { -2.4, 1.4, 2.72 })
	local function spoon(name, who, dx)
		local s = MT.box(name, { 0.14, 0.14, 1.0 }, { 0, 0, 0 }, "#D8DDE3", { mat = Enum.Material.Metal })
		table.insert(MT.rigs[who].extra, { s, dx < 0 and "armL" or "armR", CFrame.new(0, -1.15, -0.2) * CFrame.Angles(rad(70), 0, 0) })
		MT.apply(who)
	end
	spoon("spoon_d", "diddy", right ~= false and 1 or -1)
	spoon("spoon_m", "me", -1)
end

function MT.setKitchen(look)
	MT.room({ w = 24, d = 22, h = 9, wall = "#FBEAD2", floor = "#D9B98F", band = P.butter })
	MT.put("kitchen", { 0, 13, 0 }, { scale = 0.8, rot = 180 })
	MT.sign("fridge_note", { "be home", "by 6" }, { -9, 19.6, 5.0 }, 1.5, 1.1, { border = P.butter, sizes = { 0.36, 0.36 } })
	MT.look(look or "warm")
end

function MT.cake(loc, n, label)
	local x, y, z = loc[1], loc[2], loc[3]
	MT.box("cake_plate", { 2.4, 0.12, 2.4 }, { x, y, z }, "#FAFAF7", { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
	MT.box("cake_a", { 1.9, 0.8, 1.9 }, { x, y, z + 0.46 }, P.pink, { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
	MT.box("cake_b", { 1.96, 0.22, 1.96 }, { x, y, z + 0.9 }, "#FAFAF7", { shape = Enum.PartType.Cylinder, rot = { 0, 0, 90 } })
	MT.flames = {}
	for i = 1, n do
		local a = i / n * math.pi * 2
		local cx, cy = x + math.cos(a) * 0.6, y + math.sin(a) * 0.6
		MT.box("candle" .. i, { 0.12, 0.12, 0.5 }, { cx, cy, z + 1.26 }, P.sky)
		local fl = MT.box("flame" .. i, { 0.16, 0.16, 0.24 }, { cx, cy, z + 1.62 }, "#FFC23A", { neon = true, shape = Enum.PartType.Ball, shadow = false })
		table.insert(MT.flames, fl)
	end
	local g = MT.box("cake_glow", { 0.2, 0.2, 0.2 }, { x, y, z + 2.2 }, "#000000", { tr = 1, shadow = false })
	MT.light(g, "PointLight", "#FFC46B", 1.5, 10, { shadows = false })
	if label then MT.sign("cake_card", label, { x, y - 1.45, z + 0.55 }, 2.2, 0.9, { border = P.coral, sizes = { 0.6 } }) end
end

function MT.setBedroom(night)
	MT.room({ w = 14, d = 12, h = 9, wall = night and "#4A5C92" or "#DCE8F4", floor = night and "#5A6590" or "#C9B48F", ceiling = not night, lamp = 1.2 })
	MT.put("bed_b", { -2.5, 4.2, 0 }, { width = 10, rot = 90 })
	MT.box("win_f", { 3.6, 0.2, 3.6 }, { 3.4, 9.75, 5.6 }, "#FAFAF7")
	local wc = night and "#9DB7FF" or "#BFE3F7"
	local g = MT.box("win_g", { 3.1, 0.24, 3.1 }, { 3.4, 9.7, 5.6 }, wc, { neon = night })
	if night then MT.light(g, "SurfaceLight", "#9DB7FF", 2.2, 18, { face = Enum.NormalId.Front, angle = 90 }) end
	MT.sign("cal", { "FRIDAY", "13", "my test" }, night and { 3.4, 9.6, 2.4 } or { -2.5, 9.75, 6.6 }, 2.6, 3.0, { border = P.coral, colors = { P.coral, P.charcoal, "#9AA3AD" }, sizes = { 0.22, 0.42, 0.16 } })
	MT.look(night and "night" or "day")
end

function MT.setRiver(look)
	MT.ground("#9ED49A", nil, nil, Enum.Material.Grass)
	local w = MT.box("water", { 600, 16, 0.6 }, { 0, 10, -0.15 }, "#5FB4E6", { mat = Enum.Material.Glass, tr = 0.15, refl = 0.3 })
	w.CastShadow = false
	MT.box("riverbed", { 600, 16, 0.4 }, { 0, 10, -0.9 }, "#3F8FB8")
	MT.box("far_bank", { 600, 60, 0.6 }, { 0, 48, 0 }, "#98CF8E", { mat = Enum.Material.Grass })
	for i, r in ipairs({ { -4.0, 0.3, 4.2, 1.2 }, { -0.8, 0.9, 3.0, 0.9 }, { -6.6, 1.4, 2.6, 1.6 }, { 3.5, 1.2, 2.2, 0.8 }, { 7.0, 0.6, 3.2, 1.3 } }) do
		MT.box("brock" .. i, { r[3], 2.6, r[4] }, { r[1], r[2], r[4] / 2 }, "#A9B1BA", { mat = Enum.Material.Slate, rot = { 0, i * 23, 0 } })
	end
	MT.put("dock", { 22, 10, 0 }, { scale = 1.3, rot = 90 })
	for k, p in ipairs({ { -30, 34 }, { 6, 36 }, { 40, 32 }, { -44, -40 }, { 40, -44 } }) do MT.put("trees_oak", { p[1], p[2], 0 }, { height = 20, rot = k * 61 }) end
	MT.look(look or "cool")
end

function MT.setYard(old)
	MT.ground("#A9D99A", nil, nil, Enum.Material.Grass)
	MT.put("house_sub", { 0, 42, 0 }, { scale = 1.3, rot = 180 })
	for k, p in ipairs({ { -30, 26 }, { 30, 27 } }) do MT.put("trees_oak", { p[1], p[2], 0 }, { height = 20, rot = k * 61 }) end
	for i = -10, 10 do MT.box("fence" .. i, { 0.35, 0.35, 2.2 }, { i * 2, 12, 1.1 }, "#FAFAF7") end
	MT.box("fence_rail", { 41, 0.25, 0.3 }, { 0, 12, 1.6 }, "#FAFAF7")
	MT.doghouse({ 5.0, 5.5 }, old)
	MT.look("day")
end

function MT.doghouse(at, old)
	local x, y = at[1], at[2]
	MT.box("dh", { 3.0, 3.0, 2.4 }, { x, y, 1.2 }, old and "#B9A28F" or P.coral, { mat = Enum.Material.WoodPlanks })
	for sgn = -1, 1, 2 do
		local wd = Instance.new("WedgePart")
		wd.Anchored = true; wd.CanCollide = false; wd.Material = Enum.Material.SmoothPlastic; wd.Color = MT.C(old and "#6F6A66" or P.navy)
		wd.Size = Vector3.new(3.6, 1.3, 1.75)
		wd.CFrame = CFrame.new(MT.V(x + sgn * 0.85, y, 3.05)) * CFrame.Angles(0, rad(sgn * 90), 0)
		wd.Parent = MT.root()
	end
	MT.box("dh_door", { 1.4, 0.2, 1.5 }, { x, y - 1.45, 0.75 }, "#2E3138")
	MT.sign("dh_sign", { "BISCUIT" }, { x, y - 1.6, 2.05 }, 2.2, 0.6, { border = P.butter, sizes = { 0.7 } })
end

function MT.dog(at, facing)
	local m = MT.put("dog_lp", { at[1], at[2], 0 }, { height = 2.6, rot = 180 - (facing or 0) })
	MT.dogModel = m
	return m
end

function MT.setDark()
	MT.room({ w = 30, d = 14, h = 10, wall = "#2F3B66", floor = "#3A4675", ceiling = false })
	MT.look("night")
end

function MT.setWoods()
	MT.ground("#3D5E50", nil, nil, Enum.Material.Grass)
	for k, p in ipairs({ { -24, 34, 20 }, { 24, 37, 22 }, { 0, 52, 24 }, { -42, 6, 18 }, { 42, 9, 19 }, { -40, -30, 18 }, { 40, -32, 18 } }) do
		MT.put("trees_pine", { p[1], p[2], 0 }, { height = p[3], rot = k * 53 })
	end
	MT.look("night")
end

function MT.porchHouse(at, porch)
	local m = MT.put("house_sub", { at[1], at[2], 0 }, { scale = 1.3, rot = 180 })
	local cf, size = m:GetBoundingBox()
	local front = at[2] - size.Z / 2 - 0.3
	local col = porch == "green" and "#3FD27A" or "#8E9399"
	local lamp = MT.box("porch_lamp", { 0.8, 0.6, 1.0 }, { at[1] - 4.5, front, 4.6 }, col, { neon = porch == "green" })
	MT.box("porch_cap", { 1.0, 0.8, 0.16 }, { at[1] - 4.5, front, 5.2 }, "#2E3138")
	if porch == "green" then MT.light(lamp, "PointLight", col, 3, 18, { shadows = true }) end
	MT.porchLamp = lamp
	return { at[1] - 2.5, front }
end

function MT.setStreetNight(porch)
	MT.ground("#44506F", "#3E4967", 3.0)
	local door = MT.porchHouse({ 0, 34 }, porch)
	MT.put("house_sub", { -34, 24, 0 }, { scale = 1.3, rot = 180 })
	MT.put("house_sub", { 34, 24, 0 }, { scale = 1.3, rot = 180 })
	for k, p in ipairs({ { -38, 6 }, { 38, 6 } }) do MT.put("trees_pine", { p[1], p[2], 0 }, { height = 16, rot = k * 77 }) end
	MT.put("lamp_vic", { 8, 4, 0 }, { height = 13 })
	MT.look("night")
	return door
end
return "lib5 loaded"
