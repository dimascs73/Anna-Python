x = int(input())
y = int(input())
xy_map = [x, y]
t = 0
p = ["север", "запад", "юг", "восток"]
xy = [0, 0]
comand = ""
a = 0  # счетчик
while xy != xy_map:
    comand = input()
    a += 1
    if t == 4:
        t = 0
    if t == -1:
        t = 3
    if comand == "вперёд":
        xyt = int(input())
        if t == 0:
            xy[1] += xyt
        if t == 1:
            xy[0] -= xyt
        if t == 2:
            xy[1] -= xyt
        if t == 3:
            xy[0] += xyt
    if comand == "налево":
        t += 1
    if comand == "направо":
        t -= 1
    if comand == "разворот":
        t += 2
    if comand == "стоп":
        break
print(a)
print(p[t])
