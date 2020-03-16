import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    day = []
    for i in range(N):
        day.append(int(input()))
    ans = 0
    while len(day) != 1:
        gap = day[1] - 1
        check = day[1]
        while check <= day[-1]:
            if check in day:
                day.remove(check)
            check += gap
        ans += 1

    print('#{} {}'.format(t+1, ans))