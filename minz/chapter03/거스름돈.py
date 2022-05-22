money, price = map(int, input().split())
change = money - price

money_lst = [500, 100, 50, 10]
count = 0

for i in money_lst:
    count += change // i
    change %= i

print(count)