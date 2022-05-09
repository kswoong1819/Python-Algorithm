def cnt(r,c):
    global count
    nr = r
    while 1:
        nr += 1
        if nr < 0 or nr >= N or arr[nr][c] == 1:
            break
        if arr[nr][c] == 2:
            count += 1
            break


for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt(i,j)

    print('#{} {}'.format(t+1,count))