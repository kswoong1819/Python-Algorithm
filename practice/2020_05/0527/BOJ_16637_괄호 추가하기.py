import sys

sys.stdin = open('input.txt')


def calcul(arr):
    i = 1
    total = int(arr[0])
    while len(arr) > i:
        if arr[i + 1] == '.':
            i += 2
            continue
        if arr[i] == '+':
            total += int(arr[i + 1])
        if arr[i] == '-':
            total -= int(arr[i + 1])
        if arr[i] == '*':
            total *= int(arr[i + 1])
        i += 2
    return total


def go():
    global ans
    if len(mathEx) == 1:
        ans = mathEx[0]
        return
    i = 0
    while len(mathEx) - 2 > i:
        if check[i: i + 3] != [0, 0, 0]:
            i += 2
            continue
        check[i: i + 3] = [1, 1, 1]
        section = mathEx[i: i + 3]
        mathEx[i: i + 3] = [calcul(section), '.', '.']
        ans = max(ans, calcul(mathEx))
        go()
        mathEx[i: i + 3] = section
        check[i: i + 3] = [0, 0, 0]
        i += 2


N = int(input())
mathEx = list(input())

ans = -float('inf')

check = [0] * N
go()
print(ans)
