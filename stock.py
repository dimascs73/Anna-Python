day = 0
stock_buy = 0
flag = False

x = int(input())
x1 = x

while x != 0:
    x = int(input())
    if x1 > x and flag:
        break
    if x > x1 and not flag:
        stock_buy = x
        day += 1
        x1 = x
        flag = True
        continue
    if x > x1 and flag:
        day += 1
        x1 = x
    elif x < x1:
        x1 = x
        continue

print(stock_buy, end=" ")
print(x, end=" ")
print(x - stock_buy)


#
#
#
