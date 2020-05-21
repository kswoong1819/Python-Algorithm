import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K, Q = map(int, input().split())
for q in range(Q):
    x, y = map(int, input().split())

    check = 0
    while x != y:
        while x > y:
            check += 1
            x += K - 2
            x //= K
        while x < y:
            check += 1
            y += K - 2
            y //= K

    print(check)
