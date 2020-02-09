import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    score = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

    total_list = []
    for i in range(N):
        mid, final, report = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + report * 0.2
        total_list.append(total)

    find_K = total_list[K - 1]

    total_list.sort()

    for i in range(N):
        if total_list[i] == find_K:
            print('#{} {}'.format(t+1, score[i//(N//10)]))
