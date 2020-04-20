import sys

sys.stdin = open('../0416/input.txt')
input = sys.stdin.readline


def go(r, cnt):
    global ans
    if cnt == min_cnt:
        if check():
            ans = cnt
        return
    for i in range(r, H + 1):
        for j in range(1, N):
            if not ladder[i][j] + ladder[i][j - 1] + ladder[i][j + 1]:
                ladder[i][j] = 1
                go(i, cnt + 1)
                ladder[i][j] = 0


def check():
    for i in range(1, N + 1):
        t = i
        for j in range(1, H + 1):
            if ladder[j][t]:
                t += 1
            elif ladder[j][t - 1]:
                t -= 1
        if t != i:
            return False
    return True


N, M, H = map(int, input().split())
ladder = [[0] * (N + 1) for _ in range(H + 1)]
for i in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

ans = float('inf')
for min_cnt in range(4):
    go(1, 0)
    if ans != float('inf'):
        print(ans)
        break
else:
    print('-1')
