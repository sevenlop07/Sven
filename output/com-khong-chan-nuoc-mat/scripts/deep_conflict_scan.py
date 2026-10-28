import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ref_dir = 'engine/references'
files = sorted([f for f in os.listdir(ref_dir) if f.endswith('.md')])

def audit_file(fname):
    fpath = os.path.join(ref_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines()
    
    findings = []
    
    # 1. Check for legacy Track 1 / child presence allowing child in prompts
    for i, l in enumerate(lines):
        if re.search(r'Track 1\s*\(Wholesome', l, re.I):
            findings.append((i+1, "Legacy Dual-Track Child Protocol (Track 1 Wholesome allows child in prompts - conflicts with Gate 3F Absolute Zero-Minor)", l))
        if re.search(r'\bbaby\s+crib\b', l, re.I):
            findings.append((i+1, "Contains 'baby crib' (triggers Gate 3F 'baby' keyword - should be 'pine crib' or 'wooden crib')", l))
        if re.search(r'\b(child|infant|baby)\'s\s+(bedroom|room)\b', l, re.I):
            findings.append((i+1, "Contains minor word in room description (triggers Gate 3F)", l))

    # 2. Check for naked speaker syntax (speaker: " or speaker：“)
    for i, l in enumerate(lines):
        # Match lines like "Jun: “" or "Kael: “" or "Eun-ji：“"
        m = re.search(r'^\s*([A-Za-z_][\w\-]*)\s*[:：]\s*[“"]', l)
        if m:
            verb = m.group(1).lower()
            if verb not in ['says', 'speaks', 'whispers', 'snaps', 'mutters', 'cries', 'replies', 'pleads', 'retorts', 'note', 'tip', 'warning', 'example', 'prompt', 'scene', 'shot', 'setup']:
                findings.append((i+1, f"Naked speaker syntax without action verb: '{m.group(1)}:' (Gate 4G violation)", l))

    # 3. Check for [Pro] : typo
    for i, l in enumerate(lines):
        if re.search(r'\[pro\]\s*:', l, re.I):
            findings.append((i+1, "Typo '[Pro] :' instead of '[PROP]:' (Gate 3J inconsistency)", l))

    # 4. Check for rigid cutoff assertions (mandating no dialogue after 8.5s)
    for i, l in enumerate(lines):
        if re.search(r'(không|never|prohibit|cấm|bắt buộc|tuyệt đối).*?(thoại|dialogue).*?(sau|after).*?(08\.5|8\.5)', l, re.I):
            # Check if this line is BANNING the dogma or ADVOCATING the dogma
            if not re.search(r'(ban|eradicate|xóa bỏ|anti|sai lầm|strictly ban)', l, re.I):
                findings.append((i+1, "Potential rigid cutoff dogma advocacy", l))

    # 5. Check for single-shot absolutism (claiming multi-shot cuts are prohibited)
    for i, l in enumerate(lines):
        if re.search(r'(tuyệt đối không được cắt|strictly prohibit cuts|zero cuts allowed across episode)', l, re.I):
            findings.append((i+1, "Single-shot absolutism (conflicts with Track B multi-shot)", l))

    # 6. Check for Cartesian coordinate usage in prompts
    for i, l in enumerate(lines):
        if re.search(r'\[00:\d{2}.*?\].*?[XYZ]\s*:\s*[-+]?\d', l, re.I):
            findings.append((i+1, "Cartesian coordinates in prompt timeline (Gate 3H violation)", l))

    return findings

print("=== DEEP CONFLICT & CONTRADICTION SCAN ACROSS ALL REFERENCES ===")
total_findings = 0
for fname in files:
    findings = audit_file(fname)
    if findings:
        print(f"\n--- {fname} ({len(findings)} findings) ---")
        for line_no, desc, snippet in findings:
            total_findings += 1
            print(f"  Line {line_no:4d} | {desc}")
            print(f"            > {snippet.strip()[:110]}")
    else:
        print(f"\n--- {fname}: CLEAN (0 findings) ---")

print(f"\nTotal findings across all files: {total_findings}")
