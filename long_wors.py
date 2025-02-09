def print_long_words(text: str):
    a:set = { 'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y'}
    text = text.replace("," , "")
    text = text.replace("." , "")
    list1 = text.split()
    s = 0
    for char in a:
        for i in range(len(list1)):
            if char in list1[i]:
                s += 1
                if s >= 4:
                    print(list1[i])

            




print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')