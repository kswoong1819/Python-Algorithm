import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    global cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[r][c] + 1 == arr[nr][nc]:
            cnt += 1
            dfs(nr, nc)

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans_cnt = 0
    cnt_li = []
    num_li = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i, j)
            if ans_cnt <= cnt:
                ans_cnt = cnt
                cnt_li.append(cnt)
                num_li.append(arr[i][j])
    ch = cnt_li.index(ans_cnt)
    ans_num = min(num_li[ch:])

    print('#{} {} {}'.format(t+1, ans_num, ans_cnt))
