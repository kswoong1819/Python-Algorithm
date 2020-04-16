import sys
sys.stdin = open('input.txt')


def go(num):
    st = 1
    q = [num]
    while q:
        n = q.pop()
        for i in range(st, N+1):
            if ladder[n][i] == 1:
                st = i
                q.append(i)
                break
        return st


def make(k):
    global ans
    if k > 3:
        return
    for i in range(1, N+1):
        tmp = go(i)
        if i != tmp:
            break
    else:
        ans = k
    for i in ladder:
        if


N, M, L = map(int, input().split())
ladder = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    ladder[b].append([a, b+1])
    ladder[b+1].append([a, b])


ans = 0
make(0)
