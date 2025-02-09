def equation(a: str, b: str):
    coords1 = list(map(float, a.split(";")))
    x1 = coords1[0]
    y1 = coords1[1]
    coords2 = list(map(float, b.split(";")))
    x2 = coords2[0]
    y2 = coords2[1]

    if x1 == x2:
        return print(x1)
    elif y1 == y2:
        return print(y1)
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2

    print(k, b)


equation("0;0", "1;1")

equation("4;6.9", "-5.2;6.9")
