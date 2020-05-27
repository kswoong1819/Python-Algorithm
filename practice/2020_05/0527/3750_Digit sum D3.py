result = []
T = int(input())

for t in range(T):
    N = input()
    while len(N) != 1:
        nxt_N = 0
        for i in N:
            nxt_N += int(i)
        N = str(nxt_N)
    result.append(N)

for i in range(T):
    print('#{} {}'.format(i + 1, result[i]))
