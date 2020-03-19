import sys
sys.stdin = open('input.txt')


def go(k, st, ed, cur, stack):
    global ans
    if cur > ans:
        return
    if k == N:
        tmp = abs(stack[-1][0] - ed[0]) + abs(stack[-1][1] - ed[1])
        ans = min(ans, tmp + cur)
        return
    for i in range(2, N + 2):
        if visited[i]:
            continue
        visited[i] = 1
        tmp = abs(stack[-1][0] - ls[i][0]) + abs(stack[-1][1] - ls[i][1])
        stack.append(ls[i])
        go(k + 1, st, ed, cur + tmp, stack)
        stack.pop()
        visited[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    location = list(map(int, input().split()))
    ls = []
    for i in range(0, (N + 2) * 2, 2):
        ls.append([location[i], location[i + 1]])

    visited = [0] * (N + 2)
    visited[0] = visited[1] = 1
    ans = 987654321

    go(0, ls[0], ls[1], 0, [ls[0]])

    print('#{} {}'.format(t + 1, ans))
