def CaesarCipherChar(c, n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha2 = alpha.upper()
    if c.isupper():
        return alpha2[(alpha2.index(c) + n) % len(alpha2)]
    elif c.islower():
        return alpha[(alpha.index(c) + n) % len(alpha)]
    else:
        return c


def CaesarCipher(s, k):
    res = ""
    for c in s:
        res += CaesarCipherChar(c, n)
    return res


n = 4
s = input().strip()
print(CaesarCipher(s, n))
