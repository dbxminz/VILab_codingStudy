## Q1 모험가 길드 ##

N = int(input())
data = list(map(int,input().split())) # 띄어쓰기로 구분된 여러 개의 숫자 입력 값을 리스트로 받을때

# 최대값을 구해야 하므로 공포도가 낮은 사람이 그룹으로 묶어야 된다.
data.sort()

group = 0
count = 0

for i in data:
  count+=1
  if count >= i:
    group+=1
    count = 0

print(group)
  
