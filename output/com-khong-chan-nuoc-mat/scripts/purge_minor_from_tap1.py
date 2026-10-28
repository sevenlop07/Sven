import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove be_tin from [subject]: blocks
# Pattern matches be_tin [Appearance...] followed by optional comma/newlines
content = re.sub(r'be_tin\s*\[Appearance,\s*attire,\s*and\s*facial\s*features\s*Refer\s*to\s*image\s*3\],?\s*\n', '', content, flags=re.IGNORECASE)

# 2. Specific prose replacements in prompts
replacements = [
    # Diegetic acoustic triggers
    (r"infant's soft fussy coo from crib,?", "soft room tone,"),
    (r"infant's soft rhythmic breathing from crib,?", "soft cotton rustle from bedside,"),
    
    # Scene 1
    (r"beside newborn in wooden crib", "beside the wooden pine crib"),
    (r"be_tin rests safely on the firm flat organic cotton mattress in the pine crib", "the wooden pine crib stands steady with soft organic cotton bedding"),
    (r"be_tin rests undisturbed in the pine crib", "the wooden pine crib stands steady beside the bed"),
    (r"be_tin lies peacefully inside the pine crib", "the wooden pine crib rests quietly in the morning light"),
    
    # Scene 2 & 3
    (r"Inside the pine crib, be_tin lies securely on the flat mattress, stirring gently with tiny soft coos in safe undisturbed slumber\.", "The wooden pine crib stands steady with soft cotton bedding."),
    (r"Inside the pine crib, be_tin lies securely on the flat mattress in calm sleep\.", "The wooden pine crib stands steady with soft cotton bedding."),
    (r"; be_tin sleeps peacefully on the flat crib mattress\.", "; the wooden pine crib rests quietly in the morning light."),
    (r"; be_tin rests peacefully in the pine crib\.", "; the wooden pine crib stands steady beside the bed."),
    (r"be_tin rests peacefully in the pine crib\.", "the wooden pine crib stands steady beside the bed."),
    
    # Scene 4
    (r"Inside the pine crib beside the bed, be_tin lies safely on the firm flat organic cotton mattress, shielded by sturdy pine slats in calm sleep\.", "Beside the bed, the wooden pine crib stands steady with soft organic cotton bedding."),
    (r"Inside the crib, be_tin rests in serene comfort through 00:10\.0\.", "Beside the bed, the wooden pine crib rests quiet in the warm morning light through 00:10.0."),
    
    # Scene 5
    (r"Beside the bed, be_tin lies peacefully inside the pine crib, chest rising and falling in rhythmic sleep\.", "Beside the bed, the wooden pine crib rests steady in the warm morning sunlight."),
    (r"inside the pine crib, be_tin rests in calm safety\.", "the wooden pine crib stands quiet beside the bed."),
    
    # Scene 6
    (r"In the background crib, be_tin lies peacefully asleep on the firm flat mattress\.", "In the soft background, the wooden pine crib rests quiet beside the queen bed."),
    (r"In the background pine crib, be_tin sleeps peacefully through 00:10\.0\.", "In the background, the wooden pine crib stands peaceful through 00:10.0."),
    
    # Scene 7
    (r"Inside the pine crib, be_tin rests safely on the flat mattress, stirring softly in undisturbed sleep\.", "Beside the queen bed, the wooden pine crib stands steady with soft white bedding."),
    (r"; inside the pine crib, be_tin sleeps peacefully\.", "; beside the bed, the wooden pine crib remains peaceful."),
    
    # Scene 8
    (r"Inside the pine crib, be_tin lies peacefully on the flat mattress, breathing softly in calm slumber\.", "Beside the bed, the wooden pine crib stands undisturbed in the soft morning light."),
    (r"Inside the crib, be_tin sleeps peacefully\.", "The wooden pine crib stands quiet beside the bed."),
    
    # Scene 9
    (r"Inside the wooden pine crib beside the bed, be_tin lies safely on the organic cotton mattress, breathing softly in calm sleep\.", "Beside the queen bed, the wooden pine crib stands peaceful with soft cotton bedding."),
    (r"Inside the background pine crib, be_tin sleeps peacefully under the warm morning sunbeams\.", "In the background, the wooden pine crib rests quiet under the warm morning sunbeams."),
]

for pat, repl in replacements:
    content, n = re.subn(pat, repl, content)
    print(f"Replaced {n} occurrences of pattern: {pat[:40]}...")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved tap-1.html successfully.")
