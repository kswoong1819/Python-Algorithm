def DFS(v):
    visit[v] = True # 노드 방문했으니 visit 추가
    for w in G[v]:  # 해당 작업의 후행 작업 순회
        if not visit[w]:    # 만약 해당 작업이 끝나지 않았으면, 작업 수행
            DFS(w)
    stack.append(v) # 반복문이 끝이나면, V 작업의 후행 작업을 모두

for test_case in range(1, 11):
    V, E = map(int, input().split())

    G = [[] for i in range(V + 1)]  # 그래프 생성, 각 작업을 선행으로 필요로 하는 작업 리스트
    visit = [False] * (V + 1)   # 방문 배열
    in_degree = [0] * (V + 1)   #  특정 작업의 선행작업 개수를 세기 위한 배열
    stack = []  # 스택

    arr = list(map(int, input().split()))
    for i in range(0, E):
        u, v = arr[i * 2], arr[i * 2 + 1]   # 간선 입력
        G[u].append(v)  # 유향 그래프    # 그래프에 추가
        in_degree[v] += 1   # 선행작업 개수 증가

    for i in range(1, V + 1):
        if in_degree[i] == 0:   #선행작업이 없는 노드는, 작업 시작
            DFS(i)  # dfs

    print("#%d " % test_case, end='')
    print(*stack[::-1])