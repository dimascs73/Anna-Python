def squared(a: int, b: int, k: int) -> None:
    for i in range(a, b + 1):
        exponent = i**2
        if exponent % k != 0 and (a % 10 - i % 10) != 1:
            print(f"{exponent:<4}", end=" ")
        elif exponent % k != 0 and (a % 10 - i % 10) == 1:
            print(f"{exponent:<4}", end=" ")
            print(" ")
        elif exponent % k == 0 and (a % 10 - i % 10) == 1:
            print("", end=" ")
        else:
            print("", end=" ")


squared(4, 33, 9)
