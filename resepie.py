def stud() -> set:
    y = int(input())
    dt = set()
    for _ in range(y):
        student = input()
        dt.add(student)
    return dt


a = set()
b = set()
x = int(input())
a = stud()
for k in range(x - 1):
    b = stud()
    a = a & b
    b.clear()
print(*a, sep="\n")
