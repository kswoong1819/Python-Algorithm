import sys
sys.stdin = open('input.txt')

def go(k, cur):
    global result
    if visited[k][cur]:
        return
    visited[k][cur] = 1
    if k == K:
        if result < cur:
            result = cur
        return
    go(k+1, cur + score[k])
    go(k+1, cur)


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    visited = [[0]*(N*100) for _ in range(N)]

    result = 0
    go(0, 0)

    print('#{} {}'.format(t+1, result))