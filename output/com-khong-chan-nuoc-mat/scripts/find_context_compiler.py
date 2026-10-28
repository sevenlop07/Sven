import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('engine/references/4-ai-video-prompt-compiler.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '[context]' in l.lower() or 'location sheet' in l.lower():
        print(f"Line {i+1}: {l.strip()[:100]}")
