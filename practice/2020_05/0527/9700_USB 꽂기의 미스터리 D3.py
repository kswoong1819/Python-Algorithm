T = int(input())

for t in range(T):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q

    if s1 < s2:
        ans = 'YES'
    else:
        ans = 'NO'

    print('#{} {}'.format(t + 1, ans))
