import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(k, cur):
    global ans
    if ans < cur and k <= N:
        ans = cur
    if k >= N:
        return
    dfs(k + 1, cur)
    dfs(k + works[k][0], cur + works[k][1])


N = int(input())
works = []
for i in range(N):
    works.append(list(map(int, input().split())))

ans = 0
dfs(0, 0)
print(ans)
