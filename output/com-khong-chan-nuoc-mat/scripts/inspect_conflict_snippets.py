import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ref_dir = 'engine/references'

def search_snippets(fname, pattern, context_lines=2):
    fpath = os.path.join(ref_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    rx = re.compile(pattern, re.I)
    matches = []
    for i, line in enumerate(lines):
        if rx.search(line):
            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            snippet = "".join([f"  {j+1}: {lines[j]}" for j in range(start, end)])
            matches.append((i+1, snippet))
    return matches

print("=== 1. Naked speaker syntax in 1-narrative-screenplay-architecture.md ===")
for line_num, snip in search_snippets('1-narrative-screenplay-architecture.md', r'^\s*([A-Za-z_][\w]*)\s*[:：]\s*[“"]'):
    print(f"Line {line_num}:\n{snip}\n")

print("=== 2. Minor terms in 4-ai-video-prompt-compiler.md ===")
for line_num, snip in search_snippets('4-ai-video-prompt-compiler.md', r'\[subject\]:.*?(\bbe_tin\b|\bbaby\b|\binfant\b|\bnewborn\b|\bchild\b|\bkid\b)'):
    print(f"Line {line_num}:\n{snip}\n")

print("=== 3. Rigid 00:08.5 in all files ===")
for fn in ['1-narrative-screenplay-architecture.md', '3-cinematography-3d-staging.md', '4-ai-video-prompt-compiler.md']:
    snips = search_snippets(fn, r'00:08\.5')
    if snips:
        print(f"--- File: {fn} ---")
        for line_num, snip in snips:
            print(f"Line {line_num}:\n{snip}\n")

print("=== 4. Cartesian coordinates in 3-cinematography-3d-staging.md ===")
for line_num, snip in search_snippets('3-cinematography-3d-staging.md', r'[XYZ]\s*:\s*[-+]?\d'):
    print(f"Line {line_num}:\n{snip}\n")

print("=== 5. [Pro] : in 4-ai-video-prompt-compiler.md ===")
for line_num, snip in search_snippets('4-ai-video-prompt-compiler.md', r'^\s*\[Pro\]\s*:'):
    print(f"Line {line_num}:\n{snip}\n")
