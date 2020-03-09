import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    rooms = [0] * 401
    for n in range(N):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        if x % 2 == 0: x -= 1
        if y % 2 != 0: y += 1
        for k in range(x, y + 1):
            rooms[k] += 1

    print('#{} {}'.format(t + 1, max(rooms)))
