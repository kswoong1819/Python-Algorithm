N = int(input())

arr = [[0] * N for _ in range(N)]
alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

x = 0
for i in range(N):
    for j in range(N-i):
        arr[i][j] = alpa[x]
        x += 1

y = 0
for i in range(1, N):
    for j in range(-i, 0):
        arr[i][j] = y
        y += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
