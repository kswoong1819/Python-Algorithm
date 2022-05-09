import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, 0, 0, 1]
dc = [0, 1, -1, 0]


def check_num(r, c, dir):
    nr = r
    nc = c
    if arr[nr][nc] != 0:
        while 1:
            nr += dr[dir]
            nc += dc[dir]
            if nr < 0 or nr >= int(N) or nc < 0 or nc >= int(N):
                break
            if arr[r][c] != arr[nr][nc] and arr[nr][nc] != 0:
                break
            if arr[nr][nc] == 0:
                continue
            if arr[r][c] == arr[nr][nc]:
                arr[nr][nc] += arr[r][c]
                arr[r][c] = '-'
                break


def line_up(r, c, dir):
    count = 0
    nr = r
    nc = c
    if arr[nr][nc] != 0:
        while 1:
            nr += dr[dir]
            nc += dc[dir]
            if nr < 0 or nr >= int(N) or nc < 0 or nc >= int(N):
                break
            if arr[nr][nc] != 0:
                break
            if arr[nr][nc] == 0:
                count += 1
                arr[nr][nc], arr[r][c] = arr[r][c], arr[nr][nc]
    return count


T = int(input())

for t in range(T):
    N, K = input().split()
    arr = [list(map(int, input().split())) for _ in range(int(N))]

    k_list = {'up': 0, 'right': 1, 'left': 2, 'down': 3}
    dir = k_list[K]

    if dir % 2:
        for i in range(int(N)-1,-1,-1):
            for j in range(int(N)-1,-1,-1):
                check_num(i, j, dir)

        for i in range(int(N)):
            for j in range(int(N)):
                if arr[i][j] == '-':
                    arr[i][j] = 0

        while 1:
            count = 0
            for i in range(int(N)-1,-1,-1):
                for j in range(int(N)-1,-1,-1):
                    count += line_up(i, j, dir)
            if count == 0:
                break
    else:
        for i in range(int(N)):
            for j in range(int(N)):
                check_num(i, j, dir)

        for i in range(int(N)):
            for j in range(int(N)):
                if arr[i][j] == '-':
                    arr[i][j] = 0

        while 1:
            count = 0
            for i in range(int(N)):
                for j in range(int(N)):
                    count += line_up(i, j, dir)
            if count == 0:
                break

    print('#{}'.format(t + 1))
    for i in range(int(N)):
        for j in range(int(N)):
            print(arr[i][j], end=' ')
        print()