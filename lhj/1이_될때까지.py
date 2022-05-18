import numpy as np 

N, K = map(int,input().split())

count = 0 

while True:
    if N == 1:
        break
    elif N % K == 0:
        count += 1
        N = N//K
    else:
        count += 1
        N = N -1
print(count)        