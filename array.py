lst: int = [42, 17, 34, 100501]


new_list: list = list(map(int, lst))
x = len(lst)
for i in range(x):
    new_list[i] = new_list[i] % 3

print(lst)
