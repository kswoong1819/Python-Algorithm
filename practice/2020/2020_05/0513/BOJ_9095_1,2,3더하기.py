import sys

sys.stdin = open('input.txt')


def dfs(n, cur):
    global cnt
    if cur > N:
        return
    if n >= 1 and cur == N:
        cnt += 1
        return
    dfs(n + 1, cur + 1)
    dfs(n + 1, cur + 2)
    dfs(n + 1, cur + 3)


T = int(input())

for t in range(T):
    N = int(input())

    cnt = 0
    dfs(0, 0)

    print(cnt)
