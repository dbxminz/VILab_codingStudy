row, column = map(int, input().split())
maxNum = -1

for r in range(row):
    data = list(map(int, input().split()))
    if maxNum < min(data):
        maxNum = min(data)
print(maxNum)