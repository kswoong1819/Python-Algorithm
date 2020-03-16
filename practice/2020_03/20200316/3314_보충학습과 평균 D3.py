T = int(input())
res = []
for t in range(T):
    score = list(map(int, input().split()))

    total = 0
    for i in range(5):
        if score[i] < 40:
            score[i] = 40
        total += score[i]

    res.append('#{} {}'.format(t+1, total//5))
print('\n'.join(res))