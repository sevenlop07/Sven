import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ref_dir = 'engine/references'
files = [f for f in os.listdir(ref_dir) if f.endswith('.md')]

print(f"Auditing {len(files)} reference files: {files}\n")

# Check patterns for potential conflicts
checks = [
    # 1. Single-shot absolutism vs Track B
    ("Absolutist 100% Single-shot (banning cuts)", re.compile(r'\b(100%\s+unbroken|zero\s+cuts\s+allowed|strictly\s+prohibit\s+cuts|tuyệt đối không được cắt)\b', re.I)),
    
    # 2. Naked speaker syntax
    ("Naked speaker syntax in prompt code blocks (name: \")", re.compile(r'^\s*([A-Za-z_][\w]*)\s*[:：]\s*[“"]', re.M)),
    
    # 3. Child/minor terms in prompt definitions/examples
    ("Minor terms in [subject] or prompt examples", re.compile(r'\[subject\]:.*?(\bbe_tin\b|\bbaby\b|\binfant\b|\bnewborn\b|\bchild\b|\bkid\b)', re.DOTALL | re.I)),
    
    # 4. Rigid cutoff dogma (e.g. 08.5 cutoff)
    ("Rigid 08.5s cutoff dogma", re.compile(r'\b00:08\.5\b|\b8\.5s\b|\bcutoff at 8\.5\b', re.I)),
    
    # 5. Cartesian coordinates (X: +1.2m, etc.)
    ("Cartesian coordinates (Gate 3H)", re.compile(r'(?<!z-)(?<![a-zA-Z0-9_])[XYZ]\s*:\s*[-+]?\d', re.I)),
    
    # 6. Hardware jargon / Kelvin
    ("Hardware / Kelvin jargon (Gate 3D)", re.compile(r'\b(\d{4}K|\d{3,4}\s*Kelvin|24fps|ARRI|Alexa|Panavision|Sony Venice|DaVinci Resolve|Kodak Vision|f/1\.\d|f/2|ISO\s*\d+)\b', re.I)),
    
    # 7. Discrepancy between [PROP]: and [Pro] :
    ("Label [Pro] : instead of [PROP]:", re.compile(r'^\s*\[Pro\]\s*:', re.M | re.I)),
]

for name, rx in checks:
    print(f"=== CHECK: {name} ===")
    found_any = False
    for fname in files:
        fpath = os.path.join(ref_dir, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        m = rx.findall(text)
        if m:
            found_any = True
            print(f"  [{fname}] Found {len(m)} occurrences: {m[:5]}")
    if not found_any:
        print("  None found across all files.")
    print()
