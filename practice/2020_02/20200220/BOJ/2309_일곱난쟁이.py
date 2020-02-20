import sys
sys.stdin = open('input.txt')

baby = []
for i in range(9):
    baby.append(int(input()))

def go(k, start):
    if sum(a) > 100:
        return
    if k == 7:
        if sum(a) == 100:
            a.sort()
            for i in a:
                print(i)
            return
    for i in range(start, 9):
        if check[i]:
            continue
        check[i] = True
        a.append(baby[i])
        go(k+1, i+1)
        a.pop()
        check[i] = False

check = [False] * 9
a = []

go(0, 0)