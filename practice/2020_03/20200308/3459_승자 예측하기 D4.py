import sys
sys.stdin = open('input.txt')

T = int(input())
res = []
for t in range(T):
    N = int(input())

    winner = True
    x = 1
    while N > 0:
        N -= x
        if winner:
            x *= 4
        winner = not winner

    ans = 'Bob'
    if winner:
        ans = 'Alice'
    res.append('#{} {}'.format(t+1, ans))
print('\n'.join(res))