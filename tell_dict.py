t_num = int(input())
tel_dict = {}
for i in range(t_num):
    tel = input().split()
    if tel[1] in tel_dict:
        tel_dict[tel[1]].append(tel[0])
    else:
        tel_dict[tel[1]] = [tel[0]]
n = int(input())
for k in range(n):
    a = input()
    if a in tel_dict.keys():
        print(" ".join(tel_dict.get(a)))
    else:
        print("Нет в телефонной книге")
