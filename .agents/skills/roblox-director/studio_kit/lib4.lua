-- MT part 4: downloaded Creator Store assets in the sets + downloaded hair on the cast
local MT = shared.MT
MT.HAIR = { me = "hair_afro", boy = "hair_afro", diddy = "hair_black_messy", mom = "hair_straight", dad = "hair_messy", may = "hair_kardi",
	teacher = "hair_long_bangs" }
local CROWD_HAIR = { "hair_messy", "hair_black_messy", "hair_blonde_boy", "hair_pal", "hair_long_bangs", "hair_straight", "hair_afro", "hair_kardi" }
MT.HAIR_K = MT.HEAD or 1.25

local oldWho = MT.whoBase or MT.who
MT.whoBase = oldWho
function MT.who(name, at, o)
	local rig = oldWho(name, at, o)
	local base = name:match("^[^#]+")
	local h = MT.HAIR[base]
	if not h and base:match("^x%d+$") then h = CROWD_HAIR[(tonumber(base:sub(2)) * 7 + 3) % #CROWD_HAIR + 1] end
	if h and MT.LIB:FindFirstChild(h) then MT.hair(name, h, MT.HAIR_K * (o and o.scale or 1)) end
	return rig
end

function MT.town()
	MT.ground("#EFE3CB", "#E6D5B5", 3.0)
	MT.box("lawn_b", { 600, 240, 0.1 }, { 0, 140, 0.03 }, "#A9D99A", { mat = Enum.Material.Grass })
	MT.box("lawn_f", { 600, 240, 0.1 }, { 0, -146, 0.03 }, "#A9D99A", { mat = Enum.Material.Grass })
	-- back row (behind the stage) and front row (behind the camera), downloaded houses
	local backs = { { -46, "house_sub" }, { -12, "village_rp" }, { 30, "house_sub" }, { 64, "house_sub" } }
	for i, b in ipairs(backs) do
		if b[2] == "village_rp" then MT.put(b[2], { b[1] - 8, 92, 0 }, { scale = 0.9, rot = 180 })
		else MT.put(b[2], { b[1], 40, 0 }, { scale = 1.3, rot = 180 }) end
	end
	for i, x in ipairs({ -50, -10, 30, 70 }) do MT.put("house_sub", { x, -48, 0 }, { scale = 1.3, rot = 0 }) end
	for k, p in ipairs({ { -30, 26 }, { 30, 26 }, { -40, -40 }, { 40, -40 } }) do
		MT.put("trees_oak", { p[1], p[2], 0 }, { height = 22, rot = k * 47 })
	end
	for k, p in ipairs({ { -13, 4 }, { 13, 4 }, { -13, -12 }, { 13, -12 } }) do MT.put("lamp_vic", { p[1], p[2], 0 }, { height = 13 }) end
end

-- day look: softer, less washed out than lib2's first numbers
local RGB = Color3.fromRGB
MT.LOOKS.day = { b = 2.1, exp = -0.05, amb = RGB(104, 104, 114), out = RGB(128, 132, 146), soft = 0.45, top = RGB(255, 244, 228),
	atmo = { 0.26, 0.05, RGB(214, 229, 243), RGB(150, 176, 206), 0, 0.9 }, bloom = { 0.18, 24, 1.6 },
	cc = { 0.0, 0.08, 0.16, RGB(255, 251, 245) }, rays = 0.02 }
MT.LOOKS.warm.b = 1.9; MT.LOOKS.warm.exp = -0.05; MT.LOOKS.warm.bloom = { 0.22, 26, 1.5 }
MT.LOOKS.cool.b = 1.9; MT.LOOKS.cool.exp = -0.05; MT.LOOKS.cool.bloom = { 0.3, 30, 1.4 }
return "lib4 loaded"
