import sys

sys.stdin = open('input.txt')


def bfs(st, ed):
    q = [st]
    ans = 987654321
    while q:
        x, cnt = q.pop(0)
        if x == ed:
            ans = min(ans, cnt)
        if 2 * x - 1 <= K and ans > cnt and visited[2 * x] != 1:
            q.append((2 * x, cnt + 1))
            visited[2 * x] = 1
        if x + 1 <= K and ans > cnt and visited[x+1] != 1:
            q.append((x + 1, cnt + 1))
            visited[x + 1] = 1
        if x - 1 >= 0 and ans > cnt and visited[x-1] != 1:
            q.append((x - 1, cnt + 1))
            visited[x-1] = 1
    return ans


N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
print(bfs((N, 0), K))
