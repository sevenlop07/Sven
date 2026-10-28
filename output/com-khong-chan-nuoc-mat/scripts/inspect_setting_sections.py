import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('output/com-khong-chan-nuoc-mat/setting.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for section headers
sections = re.findall(r'<section[^>]*id="([^"]*)"[^>]*>(.*?)</section>', text, re.DOTALL)
print(f"Sections found: {len(sections)}")
for sid, scontent in sections:
    h = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', scontent)
    print(f"Section {sid}: {h[:3]}")

# Look for location_bedroom_4view.jpg or similar in setting.html
matches = re.findall(r'([^"\n]*location[^"\n]*)', text, re.IGNORECASE)
print(f"\nLocation image/references: {len(matches)}")
for m in set(matches[:15]):
    print("  ", m.strip())

matches_prop = re.findall(r'([^"\n]*prop_[^"\n]*)', text, re.IGNORECASE)
print(f"\nProp image/references: {len(matches_prop)}")
for m in set(matches_prop[:15]):
    print("  ", m.strip())
