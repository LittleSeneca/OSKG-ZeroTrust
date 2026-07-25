import glob, re
files = sorted(glob.glob("notes/concepts/NIST 800-207 — Ch*.md"))
for f in files:
    if "Ch2" in f or "800-207A" in f:
        continue
    print("===", f, "===")
    text = open(f, encoding='utf-8').read()
    headings = re.findall(r'^#{2,3} .+$', text, re.MULTILINE)
    for h in headings:
        print(h)
    bolds = sorted(set(re.findall(r"^\*\*([A-Za-z' ]+):\*\*", text, re.MULTILINE)))
    print("--- bold markers ---")
    print(bolds)
    print()
