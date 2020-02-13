import sys
sys.stdin = open('input.txt', 'r')

def check(n):
    ch_list = []
    for i in range(1, V+1):
        if arr[i][n] == 1:
            ch_list.append(i)
    return ch_list

def dfs(visited, A):
    for i in range(1,V+1):
        if arr[A][i] == 1 and i not in visited:
            for j in range(len(check(i))):
                if check(i)[j] not in result:
                    break
            else:
                result.append(i)
                dfs(visited, i)
    return visited

for t in range(1):
    V, E = map(int, input().split())
    lines = list(map(int, input().split()))
    arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(0, E*2, 2):
        arr[lines[i]][lines[i+1]] = 1

    li_0 = []
    for i in range(1, V+1):
        if len(check(i)) == 0:
            li_0.append(i)

    result = []
    for i in li_0:
        result.append(i)
        dfs([i], i)

    result = set(result)

    print('#{}'.format(t+1), end=' ')
    for i in result:
        print(i, end=' ')

    print()

