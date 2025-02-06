n = int(input())
arr = []
for i in range(n):
    arr += [input()]
for k in range(n - 1):
    for m in range(n - 1):
        if int(arr[m]) < int(arr[m + 1]):
            arr[m], arr[m + 1] = arr[m + 1], arr[m]
print("-------")
print(*arr, sep="\n")
