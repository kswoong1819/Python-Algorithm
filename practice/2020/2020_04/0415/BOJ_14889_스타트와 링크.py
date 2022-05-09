import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def ability(arr):
    total = 0
    for i in range(N//2):
        for j in range(N//2):
            total += S[arr[i]][arr[j]]
    return total


def team(k, st):
    global ans
    if k == N // 2:
        start = []
        link = []
        for i in range(N):
            if check[i] == 1:
                start.append(i)
            else:
                link.append(i)
        tmp = abs(ability(start) - ability(link))
        ans = min(ans, tmp)
        return
    for i in range(st, N):
        if check[i]:
            continue
        check[i] = 1
        team(k + 1, i + 1)
        check[i] = 0


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
check = [0] * N
team(0, 0)

print(ans)