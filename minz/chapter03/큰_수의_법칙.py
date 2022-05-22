N, M, K = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()

max_1 = num_lst[-1]
max_2 = num_lst[-2]
sum = 0

sum += max_1 * (M - (M // (K + 1))) 
sum += max_2 * (M // (K + 1))

print(sum)