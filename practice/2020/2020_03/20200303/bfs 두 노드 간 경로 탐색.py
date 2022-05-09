def bfs_path(graph, start, end):
    queue = [start]
    result = [start]

    if start == end:
        path.append(result)

    while queue:
        n = queue.pop(0)
        for i in graph[n]:
            if i not in path:
                bfs_path(graph, i, end)
    return result

path = []
print(bfs_path(korea, '부산', '평양'))