T = int(input())

for t in range(T):
    E, N = map(int, input().split())
    matrix = [[] for _ in range(E+2)]
    lines = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        parent, child = lines[i], lines[i+1]
        matrix[parent].append(child)

    cnt = 0
    check = [N]
    while check:
        cnt += 1
        n = check.pop()
        check += matrix[n]

    print('#{} {}'.format(t+1, cnt))