N = list(input())
N[1] = int(N[1])
print(N)

ch = ['a','b','c','d','e','f','g','h']
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

for i, j in enumerate(ch):
    if N[0] == j:
        N[0] = i + 1

x = N[0]
y = N[1]

result = []

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    result.append([nx,ny])

count = 0

for i in range(8):
    if result[i][0] >= 1 and result[i][1] >= 1:
        count += 1
print(count)