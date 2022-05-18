import numpy as np 

N = input()

plan = list(map(str,input().split()))

x, y = 1, 1
n = len(plan)

for i in plan:
    if i == 'R':
        y += 1
        if y < 1:
            y = 1
        elif y > n:
            y = n 
    elif i == 'L':
        y -= 1
        if y < 1:
            y = 1
        elif y > n:
            y = n             
    elif i == 'U':
        x -= 1
        if x < 1:
            x = 1
        elif x > n:
            x = n
    elif i == 'D':
        x += 1
        if x < 1:
            x = 1
        elif x > n:
            x = n          
            
print(x, y)