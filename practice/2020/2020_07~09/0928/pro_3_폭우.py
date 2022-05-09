# from collections import deque
#
# dr = [0, 1]
# dc = [1, 0]
#
#
# def solution(m, n, puddles):
#     answer = 0
#     matrix = [[0] * m for _ in range(n)]
#     for a, b in puddles:
#         matrix[b - 1][a - 1] = 1
#
#     q = deque()
#     q.append([0, 0, 0])
#     min_len = float('inf')
#     max_cnt = 0
#     while q:
#         r, c, cnt = q.popleft()
#         if min_len < cnt:
#             continue
#         if r == n - 1 and c == m - 1:
#             if min_len > cnt:
#                 min_len = cnt
#                 max_cnt = 1
#             else:
#                 max_cnt += 1
#         for i in range(2):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < n and 0 <= nc < m:
#                 if matrix[nr][nc] == 1:
#                     continue
#                 q.append([nr, nc, cnt + 1])
#     answer = max_cnt % 1000000007
#     return answer

def solution(m, n, puddles):
    answer = 0
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    matrix[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                continue
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    answer = matrix[n][m] % 1000000007
    return answer


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
