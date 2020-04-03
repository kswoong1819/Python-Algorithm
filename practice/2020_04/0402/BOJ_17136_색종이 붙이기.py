import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline


def find(k, s):
    global ans
    if s == 0:
        ans = min(ans, k)
        return
    if k > ans:
        return
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 and visited[i][j] == 0:
                for z in range(5, 0, -1):
                    if use[z] > 0 and i + z <= 10 and j + z <= 10:
                        cnt = 0
                        for r in range(i, i + z):
                            for c in range(j, j + z):
                                if paper[r][c] == 1 and visited[r][c] == 0:
                                    cnt += 1
                        if cnt == z * z:
                            use[z] -= 1
                            for r in range(i, i + z):
                                for c in range(j, j + z):
                                    visited[r][c] = 1
                            find(k + 1, s - z * z)
                            use[z] += 1
                            for r in range(i, i + z):
                                for c in range(j, j + z):
                                    visited[r][c] = 0
                return


paper = [list(map(int, input().split())) for _ in range(10)]
use = [0, 5, 5, 5, 5, 5]
visited = [[0] * 10 for _ in range(10)]

cnt_one = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            cnt_one += 1

ans = float('inf')
find(0, cnt_one)
if ans == float('inf'):
    print('-1')
else:
    print(ans)
