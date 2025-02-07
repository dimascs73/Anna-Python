def rests(a: int) -> list:
    new_list: list = list(map(int, lst))
    x = len(lst)
    for i in range(x):
        new_list[i] = new_list[i] % a
    return new_list


lst: int = [42, 17, 34, 100501]
print(*rests(3))
print(*lst)
