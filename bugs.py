a = float(input())
b = float(input())
c = 0
while not abs(a - b) <= 0.01:
    a = (b**2 + (a - b) ** 2) ** 0.5
    c += 1
print(c)
