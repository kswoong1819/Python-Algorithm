N = int(input())

val = 1
cnt = 0
while cnt < N*N:
    for i in range(N):
        if val > 10:
            val = 1
        print(val, end=' ')
        cnt += 1
        val += 2
    print()