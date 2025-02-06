days = [input().split() for _ in range(int(input()))]
b = {}
for name, date, month in days:
    if not month in b:
        b[month] = []
    tup = (name, date)
    b[month].append(tup)
for x in range(int(input())):
    a = input()
    if a in b.keys():
        sor = sorted(b.get(a), key=lambda x: (int(x[1]), x[0]))
        print(" ".join(map(lambda x: f"{x[0]} {x[1]}", sor)))
    else:
        print(" ")
