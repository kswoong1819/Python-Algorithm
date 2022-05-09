import sys

sys.stdin = open('input.txt')


def dfs(st, ed, visited):
    global flag
    if flag == False:
        return
    if st == ed:
        flag = False
        for i in range(len(visited)):
            print(visited[i] + 1, end=' ')
        return
    for nxt in heming[st]:
        if nxt not in visited:
            visited.append(nxt)
            dfs(nxt, ed, visited)
            visited.pop()


N, K = map(int, input().split())
heming = [[] for _ in range(N + 1)]
nums = []
for i in range(N):
    num = list(map(int, input()))
    nums.append(num)
    for j in range(i):
        cnt = 0
        for x in range(K):
            if num[x] != nums[j][x]:
                cnt += 1
        if cnt == 1:
            heming[i].append(j)
            heming[j].append(i)

st, ed = map(int, input().split())

flag = True
dfs(st - 1, ed - 1, [st - 1])

if flag:
    print('-1')
