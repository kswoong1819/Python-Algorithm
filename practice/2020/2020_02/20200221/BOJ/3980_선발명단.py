import sys
sys.stdin = open('input.txt', 'r')

def go(k, j):
    global result
    if k == 11:
        if sum(A) > result:
            result = sum(A)
            return
    for i in range(11):
        if check[i] or arr[j][i] == 0:
            continue
        check[i] = True
        A.append(arr[j][i])
        go(k+1, j+1)
        A.pop()
        check[i] = False

C = int(input())
for i in range(C):

    arr = [list(map(int, input().split())) for _ in range(11)]

    check = [False] * 11
    A = []
    result = 0
    go(0,0)
    print(result)