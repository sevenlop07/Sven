local MT = shared.MT
-- put a library hair accessory on a rig: copies the handle, keeps it on the head every frame.
-- k = uniform scale; the R6 head's HairAttachment sits 0.6 above head centre, our head is k times a standard head.
function MT.hair(name, libName, k, nudge)
	local rig = MT.rigs[name]
	local src = MT.LIB:FindFirstChild(libName)
	local h = src:FindFirstChildWhichIsA("BasePart", true):Clone()
	for _, c in ipairs(h:GetChildren()) do if c:IsA("Weld") or c:IsA("WeldConstraint") or c:IsA("JointInstance") then c:Destroy() end end
	h.Anchored = true; h.CanCollide = false; h.CanQuery = false; h.Massless = true
	local att = h:FindFirstChildWhichIsA("Attachment")
	local accCF = att and att.CFrame or (src.AttachmentPoint or CFrame.new())
	local headPoint = att and CFrame.new(0, 0.6, 0) or CFrame.new(0, 0.5, 0)
	k = k or 1
	local m = h:FindFirstChildWhichIsA("SpecialMesh")
	if m then m.Scale = m.Scale * k; m.Offset = m.Offset * k end
	h.Size = h.Size * k
	local off = CFrame.new(headPoint.Position * k) * CFrame.new((nudge or Vector3.zero)) * accCF.Rotation:Inverse() * CFrame.new(-accCF.Position * k)   -- (T(p)R)^-1 = R^-1 T(-p)
	h.Parent = rig.model
	for _, hp in ipairs(rig.hair) do hp[1]:Destroy() end
	rig.hair = {}
	table.insert(rig.extra, { h, "head", off })
	MT.apply(name)
	return h
end
return "hair fn"
