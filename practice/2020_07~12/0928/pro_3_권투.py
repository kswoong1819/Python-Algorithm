from collections import defaultdict


def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)

    for i in range(1, n + 1):
        for l in win[i]:
            lose[l] |= lose[i]
        for w in lose[i]:
            win[w] |= win[i]

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
