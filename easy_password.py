dict = []
while True:
    a = input()
    b = [a.split(":")]
    if not a:
        break
    else:
        for login, pass_w, num, g_num, name, home_cat, _ in b:
            only_name = name.split(",")
            dict += [[login, pass_w, only_name[0]]]

easy_pass = input().split(";")

for i in range(len(dict)):
    if dict[i][1] in easy_pass:
        print("To: " + dict[i][0])
        print(dict[i][2] + ", ваш пароль слишком простой, смените его.")
