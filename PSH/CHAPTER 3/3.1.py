## 큰수의 법칙 ##

n,m,k = map(int,input().split()) # 배열의 크기 N, 숫자가 더해지는 횟수 M 그리고 k 횟수
data = list(map(int,input().split()))

# 가장 큰 수 두개를 찾아야 한다.

data.sort(reverse=True)

first_n = data[0]
second_n = data[1]

# print(first_n,second_n)
result = 0
plus_number = 0
flag = 1

for i in range(m):
  plus_number += 1
  if flag % 2 == 1:
    result = result + first_n
  elif flag % 2 == 0:
    result = result + second_n
    flag += 1
    plus_number = 0

  if plus_number == k:
    flag += 1

print(result)
