def func(*all, **dic_t):
    if dic_t:
        arr: dict = {}
        arr ={'logins': {key: val for key, val in dic_t.items()}}
        return arr
    elif all:
        lst = []
        lst = [val.lower() for val in all]
        return lst


print(func("argU", "monEy", "Plus"))

print(func(key1=5, key2=2))
