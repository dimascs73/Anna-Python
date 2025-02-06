print("Вы просыпаетесь в замке")
print("Перед вами 3 двери в одной лава в другой динозавр")
print("Какую выберите (1,2,3)?")
right_answ = False

while not right_answ:
    a = input("Введите число: ")
    if a == "1":
        print("Вас сеъл динозавыр, game over")
        right_answ = False

    elif a == "2":
        print("Вы прошли дальше, выбрите следующую дверь")
        right_answ = True
    elif a == "3":
        print("Вы сгорели в лаве, game over")
        right_answ = False


if a == "2":
    print("Вы переходите в следующую комнату")
    print("Перед вами снова 3 двери в одной саблезубые тигры, а в другой в мясник")
    print("Какую выберите (правая,центральная,левая)?")
right_answ = False

while not right_answ:
    b = input("Введите слово: ")
    if b == "правая":
        print("Вас растерзали саблезубые тигры, game over")
        right_answ = False
    elif b == "левая":
        print("Вы прошли дальше, выбрите следующую дверь")
        right_answ = True
    elif b == "центральня":
        print("Вас порезал мясник, game over")
        right_answ = False


if b == "левая":
    print("Вы перешли в последнюю комнату")
    print(
        "Перед вами 3 двери, в одной ваша вторая половинка, в другой опасные испарения, а в другой злые люди"
    )
    print("Какую выберите (1,2,3)?")
right_answ = False

while not right_answ:
    a = input("Введите число: ")
    if a == "1":
        print("Вы наткнулись на людей и они избавились от вас, game over")
        right_answ = False
    elif a == "3":
        print("Вы нашли свою вторую половинку, win this game")
        right_answ = True
    elif a == "2":
        print("Вы надышались опасными испарениями, game over")
        right_answ = False
