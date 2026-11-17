-- lib7: real Roblox R6 characters. Rig parts get the proper R6 names, a Humanoid, and classic Shirt/Pants
-- (our own templates in cloth/, uploaded ids in shared.MT_CLOTH). Sleeve and shoe blocks are hidden; the clothes draw them now.
local MT = shared.MT
local CL = shared.MT_CLOTH or {}
local SHIRT_KEY = { ["#EE6F5E"] = "c1", ["#8FC9F0"] = "c2", ["#A8E0C0"] = "c3", ["#F6A6C1"] = "c4", ["#FAFAF7"] = "c5", ["#B98A5E"] = "c6",
	["#2C7A78"] = "c7", ["#E88FB0"] = "c8", ["#8FC1E8"] = "c9", ["#F2B66B"] = "c10" }
local PANTS_KEY = { ["#3D4A6B"] = "p1", ["#2E3138"] = "p2", ["#6B5B4A"] = "p3", ["#5A4A7A"] = "p4", ["#4A5A4A"] = "p5" }
local CASTK = { me = "me", boy = "me", diddy = "diddy", mom = "mom", dad = "dad", may = "may", mayor = "mayor", teacher = "teacher" }
local base = MT.makeBase or MT.make
MT.makeBase = base
function MT.make(name, st, at, facing)
	local rig = base(name, st, at, facing)
	local b = name:match("^[^#]+")
	if b == "thing" or MT.noCloth then return rig end
	local m, s = rig.model, rig.scale
	rig.armL.Name = "Left Arm"; rig.armR.Name = "Right Arm"; rig.legL.Name = "Left Leg"; rig.legR.Name = "Right Leg"
	for _, p in ipairs({ rig.armL, rig.armR, rig.legL, rig.legR }) do p.Size = Vector3.new(1, 2, 1) * s end
	for _, p in ipairs({ rig.slvL, rig.slvR, rig.shoeL, rig.shoeR }) do p.Transparency = 1 end
	local skin = Color3.fromHex(st.skin or "#E8B98F")
	rig.armL.Color = skin; rig.armR.Color = skin
	local hum = Instance.new("Humanoid")
	hum.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None
	hum.HealthDisplayType = Enum.HumanoidHealthDisplayType.AlwaysOff
	hum.Parent = m
	local sk = "shirt_" .. (CASTK[b] or SHIRT_KEY[st.shirt] or "c1")
	local pk = "pants_" .. (CASTK[b] or PANTS_KEY[st.pants] or "p1")
	local sh = Instance.new("Shirt"); sh.ShirtTemplate = CL[sk] or ""; sh.Parent = m
	local pa = Instance.new("Pants"); pa.PantsTemplate = CL[pk] or ""; pa.Parent = m
	for _, p in ipairs({ rig.torso, rig.head, rig.armL, rig.armR, rig.legL, rig.legR }) do p.CanQuery = true end
	MT.apply(name)
	return rig
end
-- preload the clothing images so the first frame of a shot is not blank
task.spawn(function()
	local list = {}
	for _, id in pairs(CL) do local d = Instance.new("Decal"); d.Texture = id; table.insert(list, d) end
	pcall(function() game:GetService("ContentProvider"):PreloadAsync(list) end)
end)
return "lib7 loaded"
