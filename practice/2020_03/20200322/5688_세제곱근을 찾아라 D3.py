import sys
sys.stdin = open('input.txt')

T = int(input())
res = []
for t in range(T):
    N = int(input())
    ans = -1
    i = 1
    while i < 10**6+1:
        if i**3 == N:
            ans = i
            break
        i += 1
    res.append('#{} {}'.format(t+1, ans))
print('\n'.join(res))