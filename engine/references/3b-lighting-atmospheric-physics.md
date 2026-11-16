# Master Lighting & Atmospheric Physics Specification (Level-2 Directorial Assistant)
File: `engine/references/3b-lighting-atmospheric-physics.md`  
SSOT Status: Master Directorial Assistant Directive for Lighting Vectors & Atmospheric Mediums

---

## 1. Architectural Purpose & The 4-Point Anti-Plastic AI Optical Standard

The **AI Lighting & Atmosphere Assistant** is a specialized capability under the Film Director (`.agents/DIRECTOR.md`). Its sole mission is to eliminate flat digital imagery, synthetic CGI/plastic sheen, and generic prompt clichés (`cinematic lighting`, `volumetric lighting`, `8k wallpaper`) by constructing mathematically plausible, physically grounded optical contracts for generative video models (Sora, Runway Gen-3, Kling, Wan 2.1, Hailuo, Veo, Seedance).

Generative video models do not understand abstract aesthetic adjectives; they calculate photons based on **source vectors, surface roughness (`matte finish`), film grain, color saturation, diffusion mediums, and shadow penumbras**.

### 1.1 The 4-Point Anti-Plastic AI Optical Contract (`Khử Mùi Nhựa AI`)
To strip away the obvious "AI-generated plastic look" (`oily/waxy skin sheen`, `fake teal-and-orange filter`, `neon oversaturation`), every Live-Action (and Grounded 3D Semi-Real) prompt must enforce four optical anchors in `Style:` and `[context]:`:
1. **Real Physical Light Emitter Over Generic `'Cinematic'`**: Never write vague `"cinematic lighting"` or `"dramatic lighting"` in `[context]:` or `Style:`. Always specify the actual physical light source (`harsh overhead fluorescent tube`, `direct low-angle tungsten desk lamp`, `filtered overcast window daylight`, `harsh natural lightning flash`, `warm gas burner flame`).
2. **`Matte Finish` & `Subtle Organic Film Grain` Over Glossy Sheen (`Strictly Zero 35mm / Lens / Hardware Numbers — Gate 3D`)**: Eliminate waxy/oily AI skin and plastic surface reflections by locking **`matte skin and surface finish with zero plastic or oily sheen, subtle organic film grain`** in Live-Action `Style:` headers (or `refined satin-matte finish with zero plastic doll sheen` in 3D Semi-Real CGI). **NEVER write `35mm`, `50mm`, `16mm`, `8K`, `24fps`, or camera hardware names (`Phantom`, `Arri`), as `35mm` causes AI generators to distort framing or render film-strip borders (`Gate 3D`)!**
3. **`Muted Natural Color Tones` Over Excessive Digital Saturation**: Raw AI diffusion models over-crank color saturation by default. Always include **`muted natural color tones`** (or `muted desaturated slate/earth tones`) to pull saturation down by one stop for an authentic theatrical negative look.
4. **Natural Micro-Imperfections**: Preserve tactile physical reality (`brushed steel, weathered stone, matte concrete, natural skin micro-texture, stray hair strands`) instead of sterile digital smoothness.

---

## 2. The 6-Point Physical Lighting Contract

Every scene's lighting profile must satisfy the **6-Point Physical Lighting Contract**:

```
[Key Light Source] ➔ [Direction & Elevation] ➔ [Descriptive Color Tone] 
        ➔ [Atmospheric Scattering Medium] ➔ [Shadow Behavior] ➔ [Light Dynamics]
```

### Point 1: Specific Key Light Source
- Ban generic "bright lights" or "studio lighting".
- Declare the exact diegetic or natural emitter:
  - *Natural*: `low-angled early dawn sunlight piercing through cracked wooden shutters`, `diffuse overcast sky overcast filtered through heavy monsoon clouds`.
  - *Practical/Diegetic*: `flickering amber kerosene lamp on bedside table`, `buzzing cool-white ceiling fluorescent tube with minor voltage fluctuation`, `dim 40-watt tungsten filament bulb hanging from bare cord`.
  - *Vehicular/Environmental*: `single sweeping halogen motorcycle headlight from off-screen alley`.

### Point 2: Direction & Elevation Vector
- Ban vague directions ("from the side") and raw numeric degree angles in video prompts.
- Declare spatial vector in natural descriptive prose:
  - `steep overhead downward key light accentuating brow ridges and collarbones`
  - `low-grazing lateral rim light sculpting jawline and cheekbones`
  - `diagonal oblique cross-light separating subject from dark background wall`

### Point 3: Descriptive Color Tone (Kelvin Number Ban)
- **STRICT PROHIBITION**: Never use numeric Kelvin ratings (`3200K`, `5600K`, `6500K`) in video prompts; diffusion models often interpret numbers as literal text or camera hardware.
- Use evocative, physical color descriptions:
  - `warm golden amber glow with burnt-orange undertones`
  - `cool pale-cyan pre-dawn tint with desaturated steel-grey shadows`
  - `sickly greenish-yellow fluorescent cast reflecting off aged tile walls`
  - `deep indigo nocturnal rim light contrasted against warm candle flicker`

### Point 4: Atmospheric Scattering Medium (Vector 5 in [context])
- Light is invisible in a pure vacuum; it becomes cinematic only when bouncing off physical suspended particles:
  - *Domestic Morning*: `microscopic golden dust motes lazily floating in sunbeams`
  - *Kitchen/Dining*: `curling wisps of fragrant steam rising from hot ceramic soup bowls into stagnant warm air`
  - *Rainy/Outdoor*: `fine airborne water droplets and heavy humid mist clinging to asphalt surfaces`
  - *Industrial/Alley*: `faint greasy haze and curling vapor plumes from street exhaust`

### Point 5: Shadow Geometry & Edge Falloff
- Direct the shadow behavior:
  - `hard diagonal slatted shadows cast across the floor by window louvers`
  - `soft feathered penumbra with gentle roll-off into velvety ambient shadows`
  - `deep silhouette contrast with crushed blacks concealing background details`

### Point 6: Light Dynamics & Micro-Fluctuations (Kinetic Light)
- Static light creates static AI actors. Living light drives video model motion:
  - `subtle rhythmic flickering of candle flame creating shifting micro-shadows along facial contours`
  - `gentle leafy shadow dappling swaying across bare shoulders under breeze`
  - `slowly sweeping headlights casting moving geometric shafts across ceiling plaster`

---

## 3. Master Lighting Palettes by Scene Archetype

### Archetype A: Intimate Domestic Melodrama (Trầm Uất Gia Đình)
```text
Key: Single warm-tungsten bare bulb hanging off-center at head height.
Direction: Diagonal downward cross-key, creating pronounced chiaroscuro on speaking character.
Tone: Warm dusty amber with muddy brown midtones.
Atmosphere: Stagnant domestic air filled with suspended microscopic dust motes.
Shadows: Long, dense shadows stretching across faded walls, leaving room corners plunged in gloom.
Dynamics: Faint electrical filament hum causing nearly imperceptible micro-vibrations in shadow edges.
```

### Archetype B: Tense Confrontation / Viral Microdrama (Xung Đột Đốp Chát)
```text
Key: Harsh overhead commercial fluorescent fixture with cold high-key spill.
Direction: Steep top-down overhead light accentuating tense brow muscles and clenched jawlines.
Tone: Sterile icy cyan-white with desaturated skin tones and clinical starkness.
Atmosphere: Bone-dry conditioned air, pristine and razor-sharp with zero softening haze.
Shadows: Heavy cavernous eye-socket shadows and sharp, brutal chin cutoffs.
Dynamics: Steady uncompromising brilliance with zero diffusion.
```

### Archetype C: Nostalgic Healing / Rural Morning (Chữa Lành Buổi Sớm)
```text
Key: Low horizontal early dawn sunlight breaking over distant foliage.
Direction: Low-grazing side-light skimming across weathered wooden surfaces.
Tone: Soft buttery gold blending into lilac-grey ambient bounce.
Atmosphere: Heavy morning dew mist rising from soil with golden ray shafts (god rays).
Shadows: Elongated, ultra-soft blue-tinted shadows rippling over textured ground.
Dynamics: Slowly expanding light footprint as the sun crests the tree line.
```

---

## 4. Model-Specific Video Rendering Rules

1. **For Kling 1.6 & Hailuo (High-Velocity / 9:16 Vertical)**:
   - Always include a **strong specular rim light** (hair light / edge kicker) to separate actors from background clutter on small mobile screens.
   - Avoid dark muddy scenes; these models lose facial likeness in crushed blacks.
2. **For Sora & Wan 2.1 (Cinematic 16:9 / Living Settle)**:
   - Excel at volumetric light shafts, subtle penumbra falloff, and multi-layered atmospheric scattering.
   - Use dynamic light fluctuations (flame flicker, swinging pendants) to maintain natural motion across 10-second takes.
