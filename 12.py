days = [input().split() for _ in range(int(input()))]
dic = {name: (date, month) for name, date, month in days}

print(dic)
