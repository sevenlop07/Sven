-- lib9 (v2 look, from the user's refs): closer, lower, wider close-ups; punchier colour; soft background depth of field.
local MT = shared.MT
local Lighting = game:GetService("Lighting")
local cu = MT.cuV2base or MT.cu
MT.cuV2base = cu
function MT.cu(name, o)
	o = table.clone(o or {})
	o.dist = (o.dist or 3.9) * 0.82
	o.height = (o.height or -0.2) - 0.55
	o.look_z = (o.look_z or -0.15) + 0.05
	o.lens = o.lens or 28
	return cu(name, o)
end
local look = MT.lookV2base or MT.look
MT.lookV2base = look
function MT.look(...)
	local r = look(...)
	local cc = Lighting:FindFirstChild("MTColor")
	if cc then cc.Saturation = cc.Saturation + 0.12; cc.Contrast = cc.Contrast + 0.06 end
	return r
end
local frame = MT.frameV2base or MT.frame
MT.frameV2base = frame
function MT.frame(id, f)
	frame(id, f)
	local dof = Lighting:FindFirstChild("MTDof") or Instance.new("DepthOfFieldEffect")
	dof.Name = "MTDof"; dof.Parent = Lighting
	local cb = MT.camBase
	if MT.dof == false or not cb then dof.Enabled = false; return end
	local cam = workspace.CurrentCamera
	local target = MT.V(cb[2][1], cb[2][2], cb[2][3])
	local d = (cam.CFrame.Position - target).Magnitude
	dof.Enabled = true
	dof.FocusDistance = d
	dof.InFocusRadius = math.max(5, d * 0.7)
	dof.FarIntensity = 0.22
	dof.NearIntensity = 0.0
end
-- hair that keeps the eyes clear (bangs over the eyes hide the new faces)
MT.HAIR.dad = "hair_black_messy"; MT.HAIR_COLOR.dad = "#2A1E18"
MT.HAIR.mom = "hair_long_bangs"; MT.HAIR_COLOR.mom = "#4A3020"
return "lib9 loaded"
