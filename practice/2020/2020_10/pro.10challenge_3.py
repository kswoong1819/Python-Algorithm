from collections import deque


def solution(n, edges):
    answer = 0
    dist = [[0] * (n+1) for _ in range(n+1)]
    print(1)
    # q = deque([[1, 0]])
    # while q:
    #     num, cnt = q.popleft()
    #     for a, b in edges:
    #         if a == num:
    #             q.append([b, cnt + 1])
    #             if dist[a][b] < cnt + 1:
    #                 dist[a][b] = cnt + 1
    # for i in dist:
    #     print(i)
    return answer


n = 250000
edges = [[1, 2], [2, 3], [3, 4]]
print(solution(n, edges))
