import sys
sys.stdin = open('input.txt')

def bfs(st, ed):
    global flag
    q = [st]
    visited = [st]
    while q:
        if ed in visited:
            flag = 1
            return
        n = q.pop()
        if n not in visited:
            visited.append(n)
        for i in range(100):
            if check[n][i] == 1 and i not in visited:
                q.append(i)

for t in range(10):
    N, K = map(int, input().split())
    ls = list(map(int, input().split()))
    check = [[0]*100 for _ in range(100)]
    for i in range(0, K*2, 2):
        check[ls[i]][ls[i+1]] = 1

    flag = 0
    bfs(0, 99)

    print('#{} {}'.format(N, flag))
