import numpy as np 

N = int(input())

a = 6*10*6*10
b = 5*9*5*9

answer = []

for i in range(1, 25):    
    answer.append((a-b)*i)

for i in range(0, 24):
    if 2 < i < 13:
        answer[i] = answer[i] + b
    elif 12 < i < 23:
        answer[i] = answer[i] + 2*b
    elif 22 < i:
        answer[i] = answer[i] + 3*b 
        
print(answer[N])