def encrypt_caesar_chars(msg: str, shift: int = 3) -> str:
    letters_L = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
    letters_U = letters_L.upper()
    if msg.islower():
        return letters_L[(letters_L.index(msg) + shift) % len(letters_L)]
    elif msg.split().isupper():
        return letters_U[(letters_U.index(msg) + shift) % len(letters_U)]
    else:
        return msg


def encrypt_caesar(msg: str, shift: int = 3):
    pass


msg = "да здравствует салат Цезарь!"
shift = 5

encrypted = encrypt_caesar(msg, shift)

print(encrypted)
