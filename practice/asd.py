def made(k, ans):
    global Max, Min
    if k == n:
        if ans > Max:
            Max = ans
        if ans < Min:
            Min = ans
        return

    for i in range(len(li)):
        if li[i] > 0:
            if i == 0:
                li[i] -= 1
                made(k + 1, ans + num[k])
                li[i] += 1
            if i == 1:
                li[i] -= 1
                made(k + 1, ans - num[k])
                li[i] += 1
            if i == 2:
                li[i] -= 1
                made(k + 1, ans * num[k])
                li[i] += 1
            if i == 3:
                li[i] -= 1
                made(k + 1, int(ans / num[k]))
                li[i] += 1

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    num = list(map(int, input().split()))
    Max = -9999999
    Min = 9999999
    made(1, num[0])
    print('#{} {}'.format(tc,Max - Min))