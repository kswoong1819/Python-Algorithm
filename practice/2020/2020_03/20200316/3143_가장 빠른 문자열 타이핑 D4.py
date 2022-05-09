import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    A, B = input().split()
    A = list(A)
    B = list(B)

    ans = 0
    while len(A) > 0:
        if A[:len(B)] == B:
            del A[:len(B)]
        else:
            del A[0]
        ans += 1

    print('#{} {}'.format(t+1, ans))