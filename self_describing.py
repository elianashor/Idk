import sys

for line in sys.stdin:
    s = line.strip()
    if s:
        ok = all(int(d) == s.count(str(i)) for i, d in enumerate(s))
        print(1 if ok else 0)
