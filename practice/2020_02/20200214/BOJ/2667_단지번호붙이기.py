import sys
sys.stdin = open('input.txt', 'r')

dr = [0,-1,0,1]
dc = [1,0,-1,0]

def dfs(r,c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 0:
            continue
        if arr[nr][nc] == 1:
            arr[nr][nc] = value
            dfs(nr, nc)


N = int(input())

arr = [[int(i) for i in input()] for _ in range(N)]

value = 1
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            value += 1
            count +=1
            arr[i][j] = value
            dfs(i,j)

sum_list = []
for i in range(2, count+2):
    result = 0
    for j in range(N):
        result += arr[j].count(i)
    sum_list.append(result)

sum_list.sort()

print(count)
for i in range(count):
    print(sum_list[i])