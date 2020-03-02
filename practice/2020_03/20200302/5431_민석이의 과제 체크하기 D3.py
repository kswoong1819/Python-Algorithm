import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    report = list(map(int, input().split()))

    arr = [i for i in range(1, N+1)]

    for i in report:
        arr.remove(i)

    print('#{} {}'.format(t+1, ' '.join(map(str, arr))))