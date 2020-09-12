def solution(n, s, a, b, fares):
    INF = float('inf')
    answer = INF
    matrix = [[INF] * (n + 1) for _ in range(n + 1)]
    for r, c, fare in fares:
        matrix[r][c] = fare
        matrix[c][r] = fare

    for i in range(1, n + 1):
        tmp = dijkstra(n, i, matrix)
        tmp2 = tmp[s] + tmp[a] + tmp[b]
        if answer > tmp2:
            answer = tmp2

    return answer


def dijkstra(n, st, matrix):
    INF = float('inf')
    visited = [0] * (n + 1)
    dist = [INF] * (n + 1)
    dist[st] = 0

    while True:
        m = INF
        N = -1
        for j in range(n + 1):
            if not visited[j] and m > dist[j]:
                m = dist[j]
                N = j
        if m == INF:
            break
        visited[N] = True
        for j in range(n + 1):
            if visited[j]:
                continue
            via = dist[N] + matrix[N][j]
            if dist[j] > via:
                dist[j] = via
    return dist


# n, s, a, b = 6, 4, 6, 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n, s, a, b = 7, 3, 4, 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

# n, s, a, b = 6, 4, 5, 6
# fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]

print(solution(n, s, a, b, fares))
