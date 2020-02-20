import sys
sys.stdin = open('input.txt')

def go(n, start):
    if n == 6:
        for i in a:
            print(i, end=' ')
        print()
    for i in range(start, k):
        if check[i]:
            continue
        check[i] = True
        a.append(S[i])
        go(n+1, i+1)
        a.pop()
        check[i] = False

while 1:
    tmp_password = list(map(int, input().split()))

    k = tmp_password[0]
    S = tmp_password[1:]
    if k == 0:
        break

    check = [False] * k
    a = []
    go(0,0)
    print()