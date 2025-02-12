def up_per(func):
    def u1(*letters):
        uper_case = [str(letter).upper() for letter in letters]
        func(*uper_case)
    return u1
print = up_per(print)





print('Нельзя ли потише?')