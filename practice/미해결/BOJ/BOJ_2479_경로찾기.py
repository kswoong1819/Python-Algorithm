import sys
sys.stdin = open('../../2020_03/20200314/input.txt')

def bfs(st, ed):
    q = [(code[st], [st])]
    result = []
    min = 987654321
    while q:
        n, path = q.pop(0)
        if n == code[ed]:
            tmp = len(path)
            if min > tmp:
                min = tmp
                result = path
        for i in range(1, N+1):
            if n != code[i] and i not in path:
                cnt = 0
                for j in range(K):
                    if n[j] != code[i][j]:
                        cnt += 1
                if cnt == 1:
                    q.append((code[i], path + [i]))
    return result


N, K = map(int, input().split())
code = [[1]]
for i in range(N):
    code.append(input())
x, y = map(int, input().split())

print(' '.join(map(str, bfs(x, y))))