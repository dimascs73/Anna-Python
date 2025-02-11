def func(*all, **dic_t):
    if dic_t:
        arr: dict = {}
        arr = {key: val for key, val in dic_t.items()}
        return arr
    elif all:
        lst = []
        lst = [val for val in all]
        return lst


print(func("argU", "monEy", "Plus"))

print(func(key1=5, key2=2))

#test of git
