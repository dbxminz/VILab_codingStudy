
N, X = int(input()), list(map(int,input().split()))

X.sort() # 정렬

count, guild = 0, 0

for i in X:
    count += 1 # 모험가 수
    if count >= i: # 모험도 수 >= 공포도 ->출발
        guild += 1 # 길드 수
        count = 0 # 리셋
        
print(guild)