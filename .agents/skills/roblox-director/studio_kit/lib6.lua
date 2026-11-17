-- MT part 6: fixes after the first check sheet
local MT = shared.MT
local RGB = Color3.fromRGB
-- 1) faces were blank when a decal had not loaded yet: preload every face once
local list = {}
for _, id in pairs(shared.MT_FACES) do local d = Instance.new("Decal"); d.Texture = id; table.insert(list, d) end
game:GetService("ContentProvider"):PreloadAsync(list)
-- 2) less haze / glow, more contrast
MT.LOOKS.day = { b = 2.0, exp = -0.12, amb = RGB(100, 100, 112), out = RGB(122, 128, 144), soft = 0.4, top = RGB(255, 244, 228),
	atmo = { 0.16, 0.0, RGB(214, 229, 243), RGB(150, 176, 206), 0, 0.25 }, bloom = { 0.1, 20, 2.2 },
	cc = { 0.0, 0.12, 0.18, RGB(255, 251, 245) }, rays = 0.0 }
MT.LOOKS.warm.atmo = { 0.12, 0, RGB(255, 236, 205), RGB(240, 190, 140), 0, 0.2 }; MT.LOOKS.warm.bloom = { 0.12, 22, 2.0 }; MT.LOOKS.warm.cc = { 0.0, 0.1, 0.12, RGB(255, 244, 228) }
MT.LOOKS.cool.atmo = { 0.22, 0.05, RGB(200, 220, 240), RGB(150, 175, 215), 0, 0.5 }; MT.LOOKS.cool.bloom = { 0.15, 24, 1.9 }
MT.LOOKS.night.bloom = { 0.35, 30, 1.2 }
-- 3) hair: Diddy gets the bacon hair dyed black; hair colour override for textured meshes
MT.HAIR.diddy = "hair_pal"
MT.HAIR.may = "hair_long_bangs"
MT.HAIR.teacher = "hair_kardi"
MT.HAIR_COLOR = { diddy = "#17141A", may = "#E8B04A" }
local oldHair = MT.hairBase or MT.hair
MT.hairBase = oldHair
function MT.hair(name, libName, k, nudge)
	local h = oldHair(name, libName, k, nudge)
	local col = MT.HAIR_COLOR[name:match("^[^#]+")]
	if col then
		local m = h:FindFirstChildWhichIsA("SpecialMesh")
		if m then m.TextureId = ""; m.VertexColor = Vector3.new(1, 1, 1) end
		if h:IsA("MeshPart") then pcall(function() h.TextureID = "" end) end
		h.Color = MT.C(col)
	end
	return h
end
-- 4) close-ups a little wider
local cu = MT.cuBase or MT.cu
MT.cuBase = cu
function MT.cu(name, o) o = o or {}; local o2 = table.clone(o); o2.dist = (o.dist or 3.9) * 1.12; return cu(name, o2) end
return "lib6 loaded"
