import sys
sys.stdin = open('list_2/input.txt', 'r')

dr = [-2,-1,0,1,2,1,0,-1]
dc = [0,1,2,1,0,-1,-2,-1]

T = int(input())

for t in range(T):
    word = input()
    arr = [['.'] * (len(word)*4 + 1) for _ in range(5)]

    for i in range(len(word)):
        r = 2
        c = 2 + (4*i)
        arr[r][c] = word[i]

        for j in range(8):
            nr = r + dr[j]
            nc = c + dc[j]
            arr[nr][nc] = '#'

    for i in range(5):
        for j in range(len(word)*4 +1):
            print(arr[i][j],end='')
        print()