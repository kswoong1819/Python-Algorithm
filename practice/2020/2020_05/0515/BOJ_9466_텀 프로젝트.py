import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000)


def dfs(v, visited):
    global ans
    check[v] = 1
    visited.append(v)
    tmp = choice[v] - 1
    if check[tmp]:
        if tmp in visited:
            for i in visited[visited.index(tmp):]:
                check[i] = 1
                ans -= 1
        return
    else:
        dfs(tmp, visited)


T = int(input())
for t in range(T):
    N = int(input())
    choice = list(map(int, input().split()))

    ans = N
    check = [0] * N
    for i in range(N):
        if check[i]:
            continue
        dfs(i, [])

    print(ans)
