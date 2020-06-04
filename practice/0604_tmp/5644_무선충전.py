import sys

sys.stdin = open('input.txt')

dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]


def charge(Ax, Ay, Bx, By):
    global result
    a_charge = []
    b_charge = []
    for i in range(A):
        x, y, c, p = router[i]
        if abs(Ax - x) + abs(Ay - y) <= c:
            a_charge.append([i, p])
        if abs(Bx - x) + abs(By - y) <= c:
            b_charge.append([i, p])

    a_charge.sort(key=lambda x: x[1], reverse=True)
    b_charge.sort(key=lambda x: x[1], reverse=True)

    used = 0
    tmp1 = 0
    for idx, P in a_charge:
        used = idx
        tmp1 += P
        break
    for idx, P in b_charge:
        if idx != used:
            tmp1 += P
            break

    tmp2 = 0
    for idx, P in b_charge:
        used = idx
        tmp2 += P
        break
    for idx, P in a_charge:
        if idx != used:
            tmp2 += P
            break

    result += max(tmp1, tmp2)


T = int(input())

for t in range(T):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    router = [list(map(int, input().split())) for _ in range(A)]

    Ax, Ay = 1, 1
    Bx, By = 10, 10
    result = 0
    charge(Ax, Ay, Bx, By)
    for i in range(M):
        Ax += dx[move_A[i]]
        Ay += dy[move_A[i]]
        Bx += dx[move_B[i]]
        By += dy[move_B[i]]
        charge(Ax, Ay, Bx, By)

    print('#{} {}'.format(t + 1, result))
