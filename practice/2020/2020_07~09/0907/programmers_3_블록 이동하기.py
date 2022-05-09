from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

q = deque()
visited = [[[0, 0], [0, 1]]]
q.append([[[0, 0], [0, 1]], 0])


def solution(board):
    answer = move(board)
    return answer


def move(board):
    N = len(board)
    while q:
        robot, cnt = q.popleft()
        for i in range(2):
            if robot[i] == [N - 1, N - 1]:
                return cnt

        for i in range(4):
            nxt = []
            for j in range(2):
                nr = robot[j][0] + dr[i]
                nc = robot[j][1] + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                if board[nr][nc] == 1:
                    break
                nxt.append([nr, nc])
                if j == 1:
                    if robot[0][0] == robot[1][0]:
                        if i == 0 or i == 1:
                            turn(robot, board, cnt, i, 0)
                    else:
                        if i == 2 or i == 3:
                            turn(robot, board, cnt, i, 1)
                    nxt.sort()
                    if nxt not in visited:
                        q.append([nxt, cnt + 1])
                        visited.append(nxt)


def turn(robot, board, cnt, d, k):
    N = len(board)
    if k == 0:
        for i in range(2):
            nx = robot[i]
            ny = [robot[i][0] + dr[d], robot[i][1]]
            tmp = [nx, ny]
            for r, c in tmp:
                if r < 0 or r >= N or c < 0 or c >= N or board[r][c] == 1:
                    break
            tmp.sort()
            if tmp not in visited:
                q.append([tmp, cnt + 1])
                visited.append(tmp)
    elif k == 1:
        for i in range(2):
            nx = [robot[i][0], dc[d] + robot[i][1]]
            ny = robot[i]
            tmp = [nx, ny]
            for r, c in tmp:
                if r < 0 or r >= N or c < 0 or c >= N or board[r][c] == 1:
                    break
            tmp.sort()
            if tmp not in visited:
                q.append([tmp, cnt + 1])
                visited.append(tmp)


# B = [[0, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 1, 1, 0, 1],
#      [1, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0]]
B = [[0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0]]
print(solution(B))
