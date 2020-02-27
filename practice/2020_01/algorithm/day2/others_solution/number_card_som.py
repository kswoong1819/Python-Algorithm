T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input()))

    li = [0] * 10
    cnt = 0
    idx = 0
    for i in range(N):
        li[a[i]] += 1

        if li[a[i]] > cnt:
            cnt = li[a[i]]
            idx = a[i]
        elif li[a[i]] == cnt:
            if a[i] > idx:
                idx = a[i]

    print(f'#{tc} {idx} {li[idx]}')