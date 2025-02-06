print(
    *[
        x**2
        for x in map(int, input().split())
        if (x % 2 != 0) and (not (x**2) % 10 == 9)
    ]
)
