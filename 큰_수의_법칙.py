import numpy as np 

N, X = list(map(int,input().split())), list(map(int,input().split()))

sort_x = np.sort(X)

if N[1] <= N[2]:
    print(sort_x[-1]*N[1])
else:
    print((sort_x[-1] * N[2] + sort_x[-2])*(N[1]//(N[2]+1)) + X[-1]*(N[1]%(N[2]+1)))