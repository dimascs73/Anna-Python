a: int = int(input())
matrix = []
i = 0
sum_of: int = 0
for row in range(a):
    rw = list(map(int, input().split(",")))
    rw[i], rw[a - 1 - i] = rw[a - 1 - i], rw[i]
    sum_of += rw[i] + rw[a - 1 - i]
    matrix.append(rw)
    i += 1
row1: int = 0
for col in range(a):
    print(" ".join(map(str, matrix[row1])))
    row1 += 1
print(sum_of)
