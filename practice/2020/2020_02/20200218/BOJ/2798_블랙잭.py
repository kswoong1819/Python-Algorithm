import sys
sys.stdin = open('input.txt', 'r')


def go(n, k):
    global ansmax
    if sum(A) > M or ansmax == M:
        return
    if k == 3:
        if sum(A) > ansmax:
            ansmax = sum(A)
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        A.append(cards[i])
        go(n, k + 1)
        A.pop()
        check[i] = False


N, M = map(int, input().split())
cards = list(map(int, input().split()))

check = [False] * N
ansmax = 0
A = []
go(N, 0)
print(ansmax)
