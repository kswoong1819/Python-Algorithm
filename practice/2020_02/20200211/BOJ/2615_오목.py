import sys
sys.stdin = open('input.txt', 'r')

dr = [-1,0,1,1]
dc = [1,1,1,0]

def check(r, c, n):
    for i in range(4):
        nr = r
        nc = c
        count = 1
        while 1:
            nr += dr[i]
            nc += dc[i]
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19:
                break
            if arr[nr][nc] != n:
                break
            if arr[nr][nc] == n:
                count += 1
            if r-dr[i] >= 0 and r-dr[i] < 19 and c-dc[i] >= 0 and c-dc[i] < 19:
                if arr[r-dr[i]][c-dc[i]] == n and count == 5:
                    count = 0
                    break
        if count == 5:

            return 'win'
    return 0

arr = [list(map(int, input().split())) for _ in range(19)]

flag = True
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            if check(i,j,1) == 'win':
                print('1')
                print(i+1, j+1)
                flag = False
                break
        if arr[i][j] == 2:
            if check(i,j,2) == 'win':
                print('2')
                print(i+1, j+1)
                flag = False
                break
if flag:
    print('0')
