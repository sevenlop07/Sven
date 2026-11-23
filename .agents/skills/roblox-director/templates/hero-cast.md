# Hero cast file (copy to `output/<series-slug>/cast/<name>.md`; one per recurring character)

Fill this once, get the user's OK, then reuse it every episode. Until it exists, the face-PNG build cap is "conditional on the hero kit" (count the face PNGs with and without the kit).

| field | value |
|---|---|
| Name | |
| Archetype & `body_profile` | `boy_athletic` / `girl_slim` / `stocky_boss` / `elder_man` / `elder_woman` / `kid_chubby` |
| Signature colour (warm-vs-cool contrast at EWS) | |
| Outfit & Micro-PBR Fabric | Shirt/Pants texture + `shirt_fabric` / `pants_fabric` (`puffer` / `wool` / `coat` / `denim` / `default`) |
| Rig & Skin Tone | Seamless R15 (`kit.build_roblox_character(rig_type="R15", ...)`) / Studio `HumanoidDescription`; Skin hex (with warm SSS) |
| Hair & 3D Accessories | `hair_style` (`curtain_part` / `elder_tufts` / `grandma_bun` / …) or `.glb` + zero-clipping 3D accessories (`earmuffs`, `add_scarf_3d`, etc.) |
| Face Kit (`Law R-LOOK`) | `make_faces_expressive.py`: `storybook_toon` (default) / `cartoon` / `rubberhose` + `age` (`youth` / `elder_man` / `elder_woman`), Anti-Glare 2D mask |
| Signature prop | |
| Never | (things they never wear or do, so episodes stay on-model; never legacy anime faces) |
| Approved by the user | date |
