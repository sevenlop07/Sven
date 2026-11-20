# Hero cast file (copy to `output/<series-slug>/cast/<name>.md`; one per recurring character)

Fill this once, get the user's OK, then reuse it every episode. Until it exists, the face-PNG build cap is "conditional on the hero kit" (count the face PNGs with and without the kit).

| field | value |
|---|---|
| Name | |
| Signature colour (reads at EWS size) | |
| Outfit (shirt / pants texture IDs) | |
| Rig | R15: Blender `kit.build_roblox_character(rig_type="R15", body_profile=…)` / Studio `HumanoidDescription`; body colours (head / torso / arms / legs RGB) |
| Face kit | FaceLibrary entry name; 19 PNGs (look.md §7.1); asset IDs in `ReplicatedStorage.FaceLibrary` |
| Signature prop | |
| Never | (things he never wears or does, so episodes stay on-model) |
| Approved by the user | date |
