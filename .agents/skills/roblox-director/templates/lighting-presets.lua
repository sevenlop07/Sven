-- v2 note (2026-11-14): old Roblox Studio route, reference only. Blender looks: k.apply_look() in scripts/rbxkit.py.
--!nocheck
--[[
LightingPresets  (ModuleScript)  -  Roblox story-reel moods, Studio only (Edit or Play mode)

Where:  put this ModuleScript in ReplicatedStorage as "LightingPresets" (the client-side shot runner needs it
        during Play; Edit-mode execute_luau can require it there too).
Why:    the 6 reference reels light by location, not by story, and 3 of 6 have dull highlights or
        crushed shadows. These moods are matched to the best-measured ref shots (see lighting-color.md).

Rules this file follows (critic.md section 4b / 6):
  * LightingStyle = Realistic + PrioritizeLightingQuality = true. Never write Lighting.Technology (deprecated).
  * Night saturation is only -0.05 (refs keep sat 0.39-0.55 at night). Never -0.3.
  * Depth of field is subtle: FarIntensity <= 0.5 everywhere ("strong DOF looks terrible").
  * No vignette here (refs have none; optional grade in the editor only).
  * Every mood sets every property it owns, so switching moods never leaves stale values.

All numbers are STARTING POINTS (HYPOTHESIS) until a test capture passes the targets in
lighting-color.md (measure.py). After calibrating, write the new numbers back into MOODS below.

API
  P.apply(name [, tweenSeconds] [, opts])  -- name = "normalDay" | "sad" | "sadWarm" | "scaryNight" | "twistReveal" | "twistNight" | "dreamMemory",
                                     -- or "mood@clock" ("normalDay@21" = the normalDay look at 9 pm). opts.clock does the same.
                                     -- The shot list's mood column and the ShotRunner's shot.mood take the same string.
  P.setTime(clock [, tweenSeconds])   -- time of day only (ClockTime 0-24), mood untouched
  P.variant(base, newName, overrides) -- register a mood variant (override any lighting/cc/... field). Define variants in
                                     -- ReplicatedStorage.EpisodeMoods (a ModuleScript that calls P.variant), never only from
                                     -- Edit-mode execute_luau: RunScenes requires EpisodeMoods so Play mode has them too.
  P.rack(fromDist, toDist [, secs] [, near]) -- rack focus: DOF on, FocusDistance fromDist -> toDist over secs (0.4-0.8)
  P.restoreDof()                      -- put back the current mood's DOF (call on the next cut after a rack)
  P.cleanFreeModelFx()                -- disables post effects / stray lights that free models bring in
  P.practical(part [, color, brightness, range, keepLook])  -- visible lamp/window that really emits light
  P.key(subjectPos, cameraPos [, color, brightness])         -- soft "cheat" key from the camera side
  P.rim(subjectPos, cameraPos [, color, brightness])         -- back light that separates the blocky silhouette
  P.focusOn(targetPart [, camera])    -- DOF focus distance = camera-to-face distance (call after placing the camera)
  P.clearShotLights()                 -- deletes the key/rim parts this module made
  P.MOODS                              -- the raw values (read them, tweak them)

Time of day: each mood has a default ClockTime (its matched ref shots). A night clock on a day mood ("normalDay@21") is
an interior lit by practicals: the sun is down, so if the room reads dark add practicals or raise Ambient 10-15, never
Lighting.Brightness (lighting-color.md 1). twistReveal at night ("twistReveal@21") keeps its warm grade with no sun.
Tweens: in Play mode tweens run. In Edit mode they may not tick (UNVERIFIED), so pass nil there.
For the twist, call apply() with NO tween exactly at the twist cut: the palette change should land on the cut.
]]

local Lighting = game:GetService("Lighting")
local TweenService = game:GetService("TweenService")
local C = Color3.fromRGB

local M = {}

--------------------------------------------------------------------------------------------------
-- MOODS  (b = HSV-V mean, s = HSV-S mean, c = gray std, w = (R-B)/255 mean, all measured on a
--         caption-free capture with measure.py; "ref" = the reference shots each mood was matched to)
--------------------------------------------------------------------------------------------------
M.MOODS = {
	-- Ref: memories 14-61 s classroom (b .68 s .45 c .25 w +.02); dog 0-23 s street + living room (b .71 s .52 w +.15).
	-- Target: b 0.62-0.72, s 0.42-0.52, c 0.22-0.26, w +0.02..+0.15.
	normalDay = {
		lighting = {
			Brightness = 2.5, ClockTime = 14.5, ExposureCompensation = 0.3, GeographicLatitude = 35,
			Ambient = C(95, 90, 85), OutdoorAmbient = C(115, 120, 130),
			EnvironmentDiffuseScale = 1, EnvironmentSpecularScale = 1, ShadowSoftness = 0.25,
		},
		atmosphere = { Density = 0.25, Offset = 0, Color = C(199, 205, 215), Decay = C(106, 112, 125), Glare = 0, Haze = 0.3 },
		bloom = { Intensity = 0.35, Size = 24, Threshold = 1.0 },
		cc = { Brightness = 0, Contrast = 0.08, Saturation = 0.05, TintColor = C(255, 248, 240) },
		dof = false,
		sunrays = { Intensity = 0.02, Spread = 0.25 },
	},

	-- Ref: bell hospital 31-50.5 s, shots #19-#23 (38.7-45.4 s): b .52 s .32 c .18 w -.09.
	-- Target: b 0.48-0.55, s 0.28-0.34, c 0.16-0.20, w -0.12..-0.05.
	sad = {
		lighting = {
			Brightness = 1.2, ClockTime = 11, ExposureCompensation = -0.4, GeographicLatitude = 35,
			Ambient = C(70, 85, 110), OutdoorAmbient = C(90, 105, 130),
			EnvironmentDiffuseScale = 0.8, EnvironmentSpecularScale = 0.6, ShadowSoftness = 0.6,
		},
		atmosphere = { Density = 0.35, Offset = 0, Color = C(150, 165, 190), Decay = C(90, 100, 125), Glare = 0, Haze = 1.0 },
		bloom = { Intensity = 0.25, Size = 30, Threshold = 1.0 },
		cc = { Brightness = 0, Contrast = -0.05, Saturation = -0.22, TintColor = C(225, 235, 255) },
		dof = { FarIntensity = 0.3, FocusDistance = 6, InFocusRadius = 8, NearIntensity = 0 },
		sunrays = false,
	},

	-- Ref: memories 118-160 s Ollie care room, shots #49-#57 (b .81 s .40 c .21 w +.26): bright, warm, blown window.
	-- Target: b 0.76-0.84, s 0.36-0.44, c 0.19-0.23, w +0.20..+0.30.
	sadWarm = {
		lighting = {
			Brightness = 3, ClockTime = 15, ExposureCompensation = 0.5, GeographicLatitude = 35,
			Ambient = C(140, 125, 105), OutdoorAmbient = C(150, 135, 115),
			EnvironmentDiffuseScale = 1, EnvironmentSpecularScale = 0.8, ShadowSoftness = 0.7,
		},
		atmosphere = { Density = 0.2, Offset = 0, Color = C(255, 232, 190), Decay = C(255, 190, 120), Glare = 0, Haze = 0.6 },
		bloom = { Intensity = 0.8, Size = 40, Threshold = 0.8 },
		cc = { Brightness = 0.02, Contrast = -0.04, Saturation = -0.08, TintColor = C(255, 238, 205) },
		dof = false,
		sunrays = false,
	},

	-- Ref: memories shop #39 98.1 s (b .14 s .55, cyan jar glow) and 98-108 s (b .27); train tunnel 46.6-72 s (b .47 s .39);
	-- town clink night 49-74 s (b .50 s .54). Dark but NOT grey.
	-- Target: b 0.25-0.35, s 0.40-0.55, c 0.17-0.21, w -0.03..+0.05, plus ONE coloured practical in frame.
	scaryNight = {
		lighting = {
			Brightness = 0.6, ClockTime = 0, ExposureCompensation = -0.5, GeographicLatitude = 35,
			Ambient = C(28, 32, 48), OutdoorAmbient = C(38, 48, 78),
			EnvironmentDiffuseScale = 0.6, EnvironmentSpecularScale = 0.8, ShadowSoftness = 0.15,
		},
		atmosphere = { Density = 0.45, Offset = 0.15, Color = C(70, 85, 125), Decay = C(30, 35, 60), Glare = 0, Haze = 1.8 },
		bloom = { Intensity = 0.6, Size = 36, Threshold = 0.85 },
		cc = { Brightness = -0.02, Contrast = 0.05, Saturation = -0.05, TintColor = C(215, 225, 255) },
		dof = { FarIntensity = 0.5, FocusDistance = 8, InFocusRadius = 6, NearIntensity = 0 },
		sunrays = false,
	},

	-- Ref: memories #45-#49 (121.3-133.3 s: b .82-.94 s .24-.48 w +.17..+.40); contrast DROPPED 0.095 at that cut.
	-- Target: b 0.80-0.92, s 0.28-0.45, c 0.15-0.20, w +0.18..+0.35. Hold 3-6 s, then change on the next scene cut
	-- (hard switch), or inside the same scene with a 0.3-0.4 s tween (lighting-color.md 4.5).
	twistReveal = {
		lighting = {
			Brightness = 3.5, ClockTime = 16.5, ExposureCompensation = 0.7, GeographicLatitude = 35,
			Ambient = C(150, 130, 110), OutdoorAmbient = C(170, 150, 125),
			EnvironmentDiffuseScale = 1, EnvironmentSpecularScale = 1, ShadowSoftness = 0.5,
		},
		atmosphere = { Density = 0.3, Offset = 0, Color = C(255, 225, 170), Decay = C(255, 170, 100), Glare = 0.3, Haze = 0.8 },
		bloom = { Intensity = 0.9, Size = 40, Threshold = 0.75 },
		cc = { Brightness = 0.03, Contrast = -0.05, Saturation = 0, TintColor = C(255, 240, 205) },
		dof = false,
		sunrays = { Intensity = 0.12, Spread = 0.5 },
	},

	-- No ref match (HYPOTHESIS): the night twist. Palette swap from scaryNight's blue to amber practical light at about the
	-- same darkness, so a night story can shift on the twist cut without daylight. Calibrate: needs a test capture.
	-- Target: b 0.38-0.48, s 0.40-0.50, c 0.17-0.21, w +0.12..+0.25 (a >=0.15 warm shift from scaryNight, C7).
	twistNight = {
		lighting = {
			Brightness = 0.8, ClockTime = 0, ExposureCompensation = -0.1, GeographicLatitude = 35,
			Ambient = C(70, 52, 40), OutdoorAmbient = C(62, 52, 60),
			EnvironmentDiffuseScale = 0.6, EnvironmentSpecularScale = 0.8, ShadowSoftness = 0.3,
		},
		atmosphere = { Density = 0.35, Offset = 0.1, Color = C(150, 110, 80), Decay = C(80, 50, 40), Glare = 0.2, Haze = 1.2 },
		bloom = { Intensity = 0.8, Size = 40, Threshold = 0.8 },
		cc = { Brightness = 0, Contrast = -0.03, Saturation = 0, TintColor = C(255, 225, 190) },
		dof = false,
		sunrays = false,
	},

	-- Ref: dog flashback crib 64.5-81 s, shots #37-#41 (b .61 s .41 c .21 w +.01, blue room + yellow glowing eyes);
	-- memories #12 30.2 s (pink sunset, "summer we met"). Use as the ONE flashback grade for the whole episode.
	-- Target: b 0.55-0.65, s 0.38-0.46, c 0.19-0.23, w -0.02..+0.05.
	dreamMemory = {
		lighting = {
			Brightness = 1.5, ClockTime = 19.5, ExposureCompensation = 0, GeographicLatitude = 35,
			Ambient = C(80, 85, 140), OutdoorAmbient = C(110, 110, 170),
			EnvironmentDiffuseScale = 1, EnvironmentSpecularScale = 0.5, ShadowSoftness = 0.8,
		},
		atmosphere = { Density = 0.4, Offset = 0, Color = C(160, 150, 200), Decay = C(190, 120, 150), Glare = 0.2, Haze = 1.2 },
		bloom = { Intensity = 0.7, Size = 44, Threshold = 0.8 },
		cc = { Brightness = 0, Contrast = -0.1, Saturation = 0, TintColor = C(235, 230, 255) },
		-- was FarIntensity 0.8 / Near 0.3 in the team draft; capped to 0.5 / 0 (critic: subtle DOF only)
		dof = { FarIntensity = 0.5, FocusDistance = 5, InFocusRadius = 4, NearIntensity = 0 },
		sunrays = { Intensity = 0.05, Spread = 0.4 },
	},
}

--------------------------------------------------------------------------------------------------
-- helpers
--------------------------------------------------------------------------------------------------
local OWN = { Atmosphere = true, Bloom = true, ColorCorrection = true, DepthOfField = true, SunRays = true }

local function ensure(className, name)
	local inst = Lighting:FindFirstChild(name)
	if inst and not inst:IsA(className) then
		inst:Destroy()
		inst = nil
	end
	if not inst then
		inst = Instance.new(className)
		inst.Name = name
		inst.Parent = Lighting
	end
	return inst
end

local function setProps(inst, props, tweenTime)
	local tweenable = {}
	for k, v in pairs(props) do
		local t = typeof(v)
		if tweenTime and tweenTime > 0 and (t == "number" or t == "Color3") then
			tweenable[k] = v
		else
			local ok, err = pcall(function() inst[k] = v end)
			if not ok then warn("[LightingPresets] could not set " .. inst.Name .. "." .. k .. ": " .. tostring(err)) end
		end
	end
	if next(tweenable) then
		TweenService:Create(inst, TweenInfo.new(tweenTime, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut), tweenable):Play()
	end
end

-- Free maps ship their own ColorCorrection / Bloom / Blur / SunRays, sometimes under the Camera too.
-- They stack on top of ours and break the targets, so switch them off (not deleted: you can turn them back on).
function M.cleanFreeModelFx()
	local n = 0
	local function scan(parent)
		for _, d in ipairs(parent:GetChildren()) do
			if d:IsA("PostEffect") and not (parent == Lighting and OWN[d.Name]) then
				d.Enabled = false
				n += 1
			elseif d:IsA("Atmosphere") and d.Name ~= "Atmosphere" then
				d:Destroy() -- only one Atmosphere can be active
				n += 1
			end
		end
	end
	scan(Lighting)
	if workspace.CurrentCamera then scan(workspace.CurrentCamera) end
	-- Free-model lights: huge ranges flatten everything (craft note, opinion). Shadows are left as they are:
	-- turning shadows on for dozens of lights can drop frames while OBS records.
	for _, l in ipairs(workspace:GetDescendants()) do
		if l:IsA("Light") and not l:GetAttribute("StoryLight") and l.Range > 20 then
			l.Range = 20
		end
	end
	print("[LightingPresets] disabled/removed " .. n .. " foreign effects")
end

--------------------------------------------------------------------------------------------------
-- apply a mood
--------------------------------------------------------------------------------------------------
local current -- name of the mood now on (for restoreDof)

function M.apply(name, tweenTime, opts)
	local base, clock = string.match(tostring(name), "^([%w_]+)@([%d%.]+)$")
	base = base or name
	clock = tonumber(clock) or (opts and opts.clock)
	local cfg = M.MOODS[base]
	assert(cfg, "unknown mood: " .. tostring(name))
	current = base

	-- renderer settings (pcall only because very old Studio builds lack the enum)
	pcall(function() Lighting.LightingStyle = Enum.LightingStyle.Realistic end)
	pcall(function() Lighting.PrioritizeLightingQuality = true end)
	Lighting.GlobalShadows = true

	setProps(Lighting, cfg.lighting, tweenTime)
	if clock then setProps(Lighting, { ClockTime = clock }, tweenTime) end
	setProps(ensure("Atmosphere", "Atmosphere"), cfg.atmosphere, tweenTime)
	setProps(ensure("BloomEffect", "Bloom"), cfg.bloom, tweenTime)
	setProps(ensure("ColorCorrectionEffect", "ColorCorrection"), cfg.cc, tweenTime)

	local dof = ensure("DepthOfFieldEffect", "DepthOfField")
	dof.Enabled = cfg.dof and true or false
	if cfg.dof then setProps(dof, cfg.dof, tweenTime) end

	local rays = ensure("SunRaysEffect", "SunRays")
	rays.Enabled = cfg.sunrays and true or false
	if cfg.sunrays then setProps(rays, cfg.sunrays, tweenTime) end

	Lighting:SetAttribute("Mood", tostring(name)) -- so a shot runner / QA can read which mood is on
end

function M.setTime(clock, tweenTime)
	setProps(Lighting, { ClockTime = clock }, tweenTime)
end

-- P.variant("sad", "sad_bathroom", { lighting = { Ambient = C(80, 90, 105) } }): copies base, overrides fields.
function M.variant(base, newName, overrides)
	local src = assert(M.MOODS[base], "unknown base mood: " .. tostring(base))
	local new = {}
	for k, v in pairs(src) do
		if type(v) == "table" then
			local t = {}
			for kk, vv in pairs(v) do t[kk] = vv end
			for kk, vv in pairs((overrides or {})[k] or {}) do t[kk] = vv end
			new[k] = t
		else
			new[k] = v
		end
	end
	for k, v in pairs(overrides or {}) do
		if type(v) ~= "table" or type(new[k]) ~= "table" then new[k] = v end -- dof = false, or a dof table on a no-DOF mood
	end
	M.MOODS[newName] = new
	M[newName] = function(tweenTime, opts) M.apply(newName, tweenTime, opts) end
	return new
end

-- one function per mood, for readability in shot lists: P.sad(), P.twistReveal() ...
for moodName in pairs(M.MOODS) do
	M[moodName] = function(tweenTime, opts) M.apply(moodName, tweenTime, opts) end
end

--------------------------------------------------------------------------------------------------
-- motivated light (refs' weakest point: interiors lit with no visible source)
--------------------------------------------------------------------------------------------------
-- Turns an existing lamp bulb / window pane / candle into a visible source that really lights the set.
-- Defaults = warm practical. Official indoor recipe for comparison: SpotLight Angle 140, Brightness 4, Range 12;
-- candle PointLight Brightness 0.7, Color 255,202,156. keepLook = true leaves the part's material/colour alone (windows).
function M.practical(part, color, brightness, range, keepLook)
	local l = part:FindFirstChild("StoryPractical") or Instance.new("PointLight")
	l.Name = "StoryPractical"
	l.Color = color or C(255, 190, 110)
	l.Brightness = brightness or 2
	l.Range = range or 14
	l.Shadows = true
	l:SetAttribute("StoryLight", true)
	l.Parent = part
	if not keepLook then
		part.Material = Enum.Material.Neon -- the bulb itself reads as the brightest thing (p99 >= 240)
		part.Color = l.Color
	end
	return l
end

local function shotLight(name, pos, aimAt, color, brightness, range, angle)
	local p = Instance.new("Part")
	p.Name = name
	p.Anchored, p.CanCollide, p.CanQuery, p.CanTouch, p.CastShadow = true, false, false, false, false
	p.Transparency = 1
	p.Size = Vector3.new(0.2, 0.2, 0.2)
	p.CFrame = CFrame.lookAt(pos, aimAt) -- Front face points at the subject
	p:SetAttribute("StoryShotLight", true)
	local s = Instance.new("SpotLight")
	s.Face = Enum.NormalId.Front
	s.Color, s.Brightness, s.Range, s.Angle, s.Shadows = color, brightness, range, angle, true
	s:SetAttribute("StoryLight", true)
	s.Parent = p
	p.Parent = workspace
	return p
end

-- Soft key from the camera side, 35 degrees off the lens axis and 2 studs above the face (HYPOTHESIS: film habit).
-- Keep it weak (1-1.5): it should lift the face decal out of the shadow, not flatten the set.
function M.key(subjectPos, cameraPos, color, brightness)
	local toCam = (cameraPos - subjectPos) * Vector3.new(1, 0, 1)
	if toCam.Magnitude < 0.01 then toCam = Vector3.new(0, 0, 1) end
	local dir = CFrame.Angles(0, math.rad(35), 0):VectorToWorldSpace(toCam.Unit)
	local pos = subjectPos + dir * 7 + Vector3.new(0, 2, 0)
	return shotLight("KeyLight", pos, subjectPos, color or C(255, 236, 214), brightness or 1.2, 14, 60)
end

-- Rim / back light: behind the subject on the far side from the camera, 3 studs up, aimed at the head.
-- Warm rim on cool scenes and cool rim on warm scenes gives the orange/blue split all 6 refs share.
function M.rim(subjectPos, cameraPos, color, brightness)
	local away = (subjectPos - cameraPos) * Vector3.new(1, 0, 1)
	if away.Magnitude < 0.01 then away = Vector3.new(0, 0, -1) end
	local pos = subjectPos + away.Unit * 6 + Vector3.new(0, 3, 0)
	return shotLight("RimLight", pos, subjectPos, color or C(255, 200, 150), brightness or 3, 18, 70)
end

function M.clearShotLights()
	for _, d in ipairs(workspace:GetChildren()) do
		if d:GetAttribute("StoryShotLight") then d:Destroy() end
	end
end

-- Rack focus (the twist move, look.md 3.3). The one allowed DOF exception: on the rack shot only, DOF is on even if the
-- mood has it off, and NearIntensity may be up to 0.5 so the near object blurs once focus leaves it (HYPOTHESIS: needs a
-- test capture). FarIntensity stays <= 0.5. Distances in studs from the camera (P.focusOn returns one).
-- In scene data: shot.rack = { at = 0.40, from = 1.2, to = 4.0, secs = 0.6 } (at = seconds into the shot); the
-- ShotRunner starts it, skips shot.focus while it runs, and calls restoreDof() on the next cut.
function M.rack(fromDist, toDist, secs, near)
	local dof = ensure("DepthOfFieldEffect", "DepthOfField")
	dof.Enabled = true
	dof.FarIntensity = math.min(dof.FarIntensity > 0 and dof.FarIntensity or 0.45, 0.5)
	dof.NearIntensity = math.min(near or 0.4, 0.5)
	dof.FocusDistance = fromDist
	dof.InFocusRadius = math.clamp(fromDist * 0.4, 0.5, 6)
	local goal = { FocusDistance = toDist, InFocusRadius = math.clamp(toDist * 0.4, 0.5, 6) }
	TweenService:Create(dof, TweenInfo.new(secs or 0.6, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut), goal):Play()
end

function M.restoreDof()
	local cfg = current and M.MOODS[current]
	local dof = ensure("DepthOfFieldEffect", "DepthOfField")
	dof.NearIntensity = 0
	dof.Enabled = cfg and cfg.dof and true or false
	if cfg and cfg.dof then setProps(dof, cfg.dof) end
end

-- DOF focus on a face. Call after the camera is placed; call again every frame if the camera moves a lot.
function M.focusOn(target, camera)
	camera = camera or workspace.CurrentCamera
	local dof = Lighting:FindFirstChild("DepthOfField")
	if not (dof and camera and target) then return end
	local d = (camera.CFrame.Position - target.Position).Magnitude
	dof.FocusDistance = d
	dof.InFocusRadius = math.clamp(d * 0.4, 1.5, 6) -- face sharp, set softly out of focus
	return d
end

-- Night variants of the sad moods (HYPOTHESIS, from a round-3 plan; calibrate). At night, C9 (sat >= 0.40, one coloured
-- glow) beats the day presets' saturation: `sad` sits at 0.28-0.34, so a sad night scene uses sad_night.
M.variant("sad", "sad_night", { lighting = { ClockTime = 22, Brightness = 0.8 }, cc = { Saturation = -0.08 } })
M.variant("sadWarm", "sadWarm_night", { lighting = { ClockTime = 21 }, cc = { Saturation = -0.04 } })

return M

--[[ Usage through the Studio MCP (execute_luau, Edit mode):

local P = require(game.ReplicatedStorage.LightingPresets)
P.cleanFreeModelFx()                         -- once, after inserting a free map
P.apply("sad")                               -- instant
P.apply("normalDay@21")                      -- the day look at 9 pm (warm interior lit by practicals)
P.rack(1.2, 4.0, 0.6)                        -- twist rack focus: smudge on the glass -> face; P.restoreDof() on the next cut
P.practical(workspace.Classroom.Lamp.Bulb)   -- visible source in every interior shot
local cam = workspace.CurrentCamera
P.key(workspace.Hero.Head.Position, cam.CFrame.Position)
P.rim(workspace.Hero.Head.Position, cam.CFrame.Position, Color3.fromRGB(150, 190, 255))
P.focusOn(workspace.Hero.Head)
-- ... capture ... then:
P.clearShotLights()
]]
