import numpy as np 

N = list(map(int, input())) #리스트로 받고, 안의 값은 정수로 변환
# print(N)

head = None
head_count = None

for e, i in enumerate(N):
    if i == 0: #리스트 받아서 맨 앞이 0이면 pass
        pass
    elif i != 0: # 시작 값이 0이 아닌 정수로 시작할 수 있도록
        head = i # 헤드 저장
        head_count = e # 리스트 arg 저장
        break
# print(head, head_count)       
        
for i in range(head_count+1, len(N)):
    if head == 1: #헤드가 1이면 바로 다음은 더해야 된다(ex.01006)
        head += N[i]
    
    elif N[i] == 0 or N[i] == 1: #헤드 이후 0, 1 값은 더해 한다(ex.02105)
        head += N[i]
            
    else:
        head = head * N[i] # 아니면 곱셈
        
print(head)
        