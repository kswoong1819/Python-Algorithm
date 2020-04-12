import sys

sys.stdin = open('input.txt')
import copy
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def track(k):
    global ans
    if k == 5:
        tmp = game(A)
        if ans < tmp:
            ans = tmp
        return
    for i in range(4):
        A.append(i)
        track(k + 1)
        A.pop()


def game(A):
    matrix = copy.deepcopy(arr)
    for a in A:
        check = []
        cnt = 0
        for i in range(N):
            for j in range(N):
                ni, nj = change_ij(a, i, j)
                if matrix[ni][nj] != 0:
                    nr, nc = ni, nj
                    while 1:
                        nr += dr[a]
                        nc += dc[a]
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            break
                        if matrix[nr][nc] == matrix[ni][nj] and [nr, nc] not in check:
                            cnt += 1
                            matrix[nr][nc] *= 2
                            matrix[ni][nj] = 0
                            break
                        elif matrix[nr][nc] == 0:
                            cnt += 1
                            matrix[nr][nc] = matrix[ni][nj]
                            matrix[ni][nj] = 0
                            ni, nj = nr, nc
                        elif matrix[nr][nc] != matrix[ni][nj]:
                            break
                    check.append([nr, nc])
        if cnt == 0:
            break
    return find(matrix)


def find(matrix):
    tmp_max = 0
    for i in range(N):
        n = max(matrix[i])
        if tmp_max < n:
            tmp_max = n
    return tmp_max


def change_ij(a, i, j):
    if a == 0:
        return i, N - j - 1
    if a == 1:
        return N - j - 1, i
    if a == 2:
        return i, j
    if a == 3:
        return j, i


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

A = []
ans = 0
track(0)

print(ans)
