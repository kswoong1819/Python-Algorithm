import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(arr):
    for i in range(N-1):
        if abs(arr[i+1] - arr[i]) > 1:
            return 0
        if arr[i+1] - arr[i] == 1:
            if (i+1)-L >= 0:
                for j in range(i, i-L, -1):
                    if arr[i] != arr[j] or visited[j] == 1:
                        return 0
                    visited[j] = 1
            else:
                return 0
        if arr[i] - arr[i+1] == 1:
            if i + L < N:
                for j in range(i+1, i+L+1):
                    if arr[i+1] != arr[j] or visited[j] == 1:
                        return 0
                    visited[j] = 1
            else:
                return 0
    return 1


N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


cnt = 0
for i in range(N):
    visited = [0] * N
    cnt += check(matrix[i])

for i in range(N-1):
    for j in range(i+1, N):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(N):
    visited = [0] * N
    cnt += check(matrix[i])

print(cnt)