N = 10**6
check = [True] * (N+1)
for i in range(2, N+1):
    if check[i]:
        for j in range(i+i, N, i):
            check[j] = False
for i in range(2, N):
    if check[i]:
        print(i, end=' ')