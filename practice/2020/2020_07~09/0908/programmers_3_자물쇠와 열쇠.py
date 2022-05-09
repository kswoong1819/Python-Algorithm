from collections import deque

q = deque()


def solution(key, lock):
    lock_blank = 0
    n = len(key[0]) - 1
    m = len(lock[0])
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                lock_blank += 1
    rot(key, n + 1)
    answer = check(lock, lock_blank, n, m, m + n)
    return answer


def rot(key, n):
    keys = [[] for _ in range(4)]
    for i in range(n):
        for j in range(n):
            if key[i][j] == 1:
                keys[0].append([i, j])
            if key[-1 - j][i] == 1:
                keys[1].append([i, j])
            if key[-1 - i][-1 - j] == 1:
                keys[2].append([i, j])
            if key[j][-1 - i] == 1:
                keys[3].append([i, j])
    for i in range(4):
        q.append(keys[i])


def check(lock, blank, n, m, t):
    while q:
        point = q.popleft()
        for i in range(t):
            for j in range(t):
                nxt = []
                for a in range(len(point)):
                    nr = point[a][0] - n + i
                    nc = point[a][1] - n + j
                    if nr < 0 or nr >= m or nc < 0 or nc >= m:
                        continue
                    nxt.append([nr, nc])
                # print(nxt)
                if len(nxt) == blank:
                    for r, c in nxt:
                        if lock[r][c] == 1:
                            break
                    else:
                        return True
    return False


# key = [[0, 0, 0],
#        [1, 0, 0],
#        [0, 1, 1]]
# lock = [[1, 1, 1],
#         [1, 1, 0],
#         [1, 0, 1]]
key = [[0, 0, 0],
       [1, 1, 0],
       [0, 1, 1]]
lock = [[1, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]
print(solution(key, lock))
