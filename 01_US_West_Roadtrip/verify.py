with open('/Users/jingyilu/.openclaw/workspace/roadtrip-usa-2026.html', 'r') as f:
    c = f.read()

sections = ['overview', 'route', 'daily', 'weather', 'clothes', 'mexico', 'apps']
tabs = ['overview', 'route', 'daily', 'weather', 'clothes', 'mexico', 'apps']

print("Sections:")
for s in sections:
    found = 'id="' + s + '"' in c
    print(f"  {s}: {'OK' if found else 'MISSING'}")

print("\nTabs:")
for t in tabs:
    found = "showTab('" + t + "')" in c
    print(f"  {t}: {'OK' if found else 'MISSING'}")

print(f"\nTotal chars: {len(c)}")
print(f"Has showTab with 穿衣: {'穿衣' in c and 'showTab' in c}")
print(f"Has weather section: {'id=\"weather\"' in c}")
print(f"Has gear section: {'id=\"gear\"' in c}")
