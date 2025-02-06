days = [input().split() for _ in range(int(input()))]
b = {}
for name, date, month in days:
    if month not in b:
        b[month.strip()] = []
    val = (name.strip(), date.strip())
    b[month.strip()].append(val)
for x in range(int(input())):
    a = sorted(b.get(input(), ""), key=lambda x: (int(x[1]), x[0]))
    print(" ".join(map(lambda x: f"{x[0]} {x[1]}", a)))
