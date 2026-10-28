import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        r"thin hungry newborn whimper off-screen from wooden crib,?",
        "soft cotton rustle from wooden pine crib,"
    ),
    (
        r"In the background pine crib beside the bed, be_tin lies safely on the firm flat organic cotton mattress in undisturbed slumber, breathing softly with tiny fists curled beside rosy cheeks\.",
        "In the background beside the bed, the wooden pine crib stands steady with soft organic cotton bedding."
    ),
    (
        r"In the soft-focus background inside the pine crib, be_tin rests safely on the flat mattress, shielded by sturdy vertical pine slats in serene tranquility\.",
        "In the soft-focus background, the wooden pine crib stands steady with soft white bedding."
    ),
    (
        r"Inside the background pine crib, be_tin lies peacefully under warm sunbeams, chest rising and falling rhythmically in undisturbed sleep through 00:10\.0\.",
        "Beside the bed, the wooden pine crib stands peaceful under warm sunbeams through 00:10.0."
    ),
    (
        r"Inside the pine crib, be_tin lies flat on the cotton mattress, sleeping peacefully with tiny soft breaths\.",
        "Beside the bed, the wooden pine crib stands undisturbed with soft cotton bedding."
    ),
    (
        r"; be_tin sleeps peacefully in the pine crib undisturbed\.",
        "; the wooden pine crib stands undisturbed beside the bed."
    ),
    (
        r"be_tin sleeps peacefully in the pine crib undisturbed\.",
        "the wooden pine crib stands undisturbed beside the bed."
    ),
]

for pat, repl in replacements:
    content, n = re.subn(pat, repl, content)
    print(f"Replaced {n} occurrences of: {pat[:40]}...")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved tap-1.html successfully.")
