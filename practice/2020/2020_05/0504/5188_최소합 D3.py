dr = [0, 1]
dc = [1, 0]

def dfs(r, c, cur):
    global ans
    if ans < cur:
        return
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if nr == N-1 and nc == N-1:
            ans = min(ans, cur + arr[nr][nc])
            return
        dfs(nr, nc, cur + arr[nr][nc])


T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = float('inf')
    dfs(0, 0, arr[0][0])

    print('#{} {}'.format(t+1, ans))