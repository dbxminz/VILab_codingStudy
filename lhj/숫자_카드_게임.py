import numpy as np 

N, M = map(int,input().split())

cards = []
for i in range(N):
    card = list(map(int,input().split()))
    cards.append(card)

big = []

for i in range(N):
    big.append(np.min(cards[i]))

print(np.sort(big)[-1])