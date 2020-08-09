import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))

    cnt = 0
    i = 0
    while 1:
        if max(priority) == priority[i]:
            cnt += 1
            if i == M:
                print(cnt)
                break
            else:
                priority.pop(i)
                M -= 1
        else:
            tmp = priority.pop(i)
            priority.append(tmp)
            if i == M:
                M = N - (cnt + 1)
            else:
                M -= 1
