import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    matrix = [[str(1)]*N for x in range(N)]
    num_list = [str(i) for i in range(2, N*N+1)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    r = c = count = 0
    next_N = N-1
    for k in range(N*2-1):
        if k < 3:
            for _ in range(next_N):
                nr = r + dr[k%4]
                nc = c + dc[k%4]
                matrix[nr][nc] = num_list[count]
                count += 1
                r, c = nr, nc
        else:
            if k % 2 != 0:
                next_N -= 1
            for _ in range(next_N):
                nr = r + dr[k%4]
                nc = c + dc[k%4]
                matrix[nr][nc] = num_list[count]
                count += 1
                r, c = nr, nc

    print('#{}'.format(t+1))
    for ad in range(N):
        print(' '.join(matrix[ad]))