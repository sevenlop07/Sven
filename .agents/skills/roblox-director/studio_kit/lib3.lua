-- MT part 3: asset library (downloaded Creator Store models), cleaned and placeable
local MT = shared.MT
local SS = game:GetService("ServerStorage")
local lib = SS:FindFirstChild("MTLib") or Instance.new("Folder")
lib.Name = "MTLib"; lib.Parent = SS
MT.LIB = lib

-- strip anything that could run or make noise; anchor everything
function MT.clean(inst)
	local n = 0
	for _, d in ipairs(inst:GetDescendants()) do
		if d:IsA("LuaSourceContainer") or d:IsA("Sound") or d:IsA("ProximityPrompt") or d:IsA("ClickDetector") or d:IsA("Tool")
			or d:IsA("Humanoid") and not inst:GetAttribute("keepHumanoid") or d:IsA("ParticleEmitter") or d:IsA("Fire") or d:IsA("Smoke") or d:IsA("Sparkles") then
			d:Destroy(); n += 1
		elseif d:IsA("BasePart") then
			d.Anchored = true; d.CanCollide = false; d.CanTouch = false; d.CanQuery = false
		end
	end
	return n
end

function MT.cleanLib()
	local out = {}
	for _, m in ipairs(lib:GetChildren()) do
		local n = MT.clean(m)
		local ok, cf, size = pcall(function() if m:IsA("Model") then return m:GetBoundingBox() end end)
		table.insert(out, string.format("%s: removed %d, size %s", m.Name, n, ok and size and tostring(Vector3.new(math.floor(size.X), math.floor(size.Y), math.floor(size.Z))) or "?"))
	end
	return table.concat(out, "\n")
end

-- place a library model: put(name, {x,y,z}, {height=, width=, rot=deg around up, ground=true})
function MT.put(name, at, o)
	o = o or {}
	local src = lib:FindFirstChild(name)
	if not src then error("no library model " .. name) end
	local m = src:Clone()
	if not m:IsA("Model") then local mm = Instance.new("Model"); m.Parent = mm; m = mm end
	m.Parent = MT.root()
	local cf, size = m:GetBoundingBox()
	local s = 1
	if o.height then s = o.height / size.Y elseif o.width then s = o.width / math.max(size.X, size.Z) elseif o.scale then s = o.scale end
	if s ~= 1 then m:ScaleTo(m:GetScale() * s); cf, size = m:GetBoundingBox() end
	local pivot = m:GetPivot()
	local offset = pivot.Position - cf.Position
	local target = MT.V(at[1], at[2], (at[3] or 0)) + Vector3.new(0, size.Y / 2, 0)
	m:PivotTo(CFrame.new(target + offset) * CFrame.Angles(0, math.rad(o.rot or 0), 0) * (pivot - pivot.Position))
	return m
end

-- show one library model alone on a grey floor and frame the camera on it (for picking assets)
function MT.show(name)
	MT.clear()
	MT.box("floor", { 400, 400, 1 }, { 0, 0, -0.5 }, "#D9DDE3")
	MT.look("day")
	local m = MT.put(name, { 0, 0, 0 })
	local cf, size = m:GetBoundingBox()
	local r = math.max(size.X, size.Y, size.Z)
	local cam = workspace.CurrentCamera
	cam.CameraType = Enum.CameraType.Scriptable
	cam.FieldOfView = 50
	cam.CFrame = CFrame.lookAt(cf.Position + Vector3.new(r * 0.75, r * 0.55, r * 0.95), cf.Position)
	return tostring(size)
end
return "lib3 loaded"
