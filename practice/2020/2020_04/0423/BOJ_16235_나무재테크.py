import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def grow():
    global tree_cnt
    spread = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if len(tree[i][j]):
                tree[i][j].sort()
                for z in range(len(tree[i][j])):
                    if st_food[i][j] - tree[i][j][z] >= 0:
                        st_food[i][j] -= tree[i][j][z]
                        tree[i][j][z] += 1
                        if tree[i][j][z] % 5 == 0:
                            spread.append([i, j])
                    else:
                        while z != len(tree[i][j]):
                            st_food[i][j] += tree[i][j][z] // 2
                            tree_cnt -= 1
                            tree[i][j].pop(z)
                        break
    fall(spread)
    winter()

def fall(trees):
    global tree_cnt
    q = deque()
    q += trees
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 < nr <= N and 0 < nc <= N:
                tree_cnt += 1
                tree[nr][nc].append(1)

def winter():
    for i in range(1, N+1):
        for j in range(1, N+1):
            st_food[i][j] += add_food[i][j]



N, M, K = map(int, input().split())
st_food = [[0] * (N+1)] + [[0] + [5] * N for n in range(N)]
add_food = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for n in range(N)]
tree = [[[] for i in range(N+1)] for _ in range(N + 1)]

tree_cnt = 0
for m in range(M):
    x, y, z = map(int, input().split())
    tree[x][y].append(z)
    tree_cnt += 1
for i in range(K):
    grow()

print(tree_cnt)