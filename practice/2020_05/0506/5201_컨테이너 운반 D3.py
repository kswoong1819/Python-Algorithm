T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    cargo.sort()
    cargo.reverse()
    truck.sort()
    truck.reverse()
    result = 0
    for i in range(M):
        for j in range(N):
            if truck[i] >= cargo[j]:
                result += cargo[j]
                cargo[j] = 51
                break

    print('#{} {}'.format(t + 1, result))
