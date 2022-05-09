def add(A, B):
    return A + B


T = int(input())
res = []
for t in range(T):
    A, B = map(int, input().split())
    res.append('#{} {}'.format(t + 1, add(A, B)))
print('\n'.join(res))