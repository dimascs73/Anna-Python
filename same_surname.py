surnames_all = set()
surnames_uniq = set()
number = int(input())
for i in range(number):
    name = input()
    if name in surnames_uniq:
        surnames_all.add(name)
    else:
        surnames_uniq.add(name)
n = number - (len(surnames_uniq) - len(surnames_all))
print(n)
