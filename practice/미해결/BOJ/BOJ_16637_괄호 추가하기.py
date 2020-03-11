import sys

sys.stdin = open('../../2020_03/20200311/input.txt')
import copy


def calcul(n, m):
    i = 0
    while i != n - 1:
        if m[i] == '+':
            m[i + 1] = int(m[i - 1]) + int(m[i + 1])
        if m[i] == '-':
            m[i + 1] = int(m[i - 1]) - int(m[i + 1])
        if m[i] == '*':
            m[i + 1] = int(m[i - 1]) * int(m[i + 1])
        i += 1
    return m[n - 1]


def bracket(n, m):
    i = 0
    while n - 1 != i:
        if m[i] == '(':
            brac = m[i + 1:i + 4]
            tmp = calcul(3, brac)
            del m[i + 1:i + 5]
            m[i] = tmp
            n -= 4
            continue
        i += 1
    tmp = calcul(n, m)
    return tmp


def make_brack(n, m, st):
    global ans
    if n == 1:
        ans = m[0]
        return
    m_2 = copy.deepcopy(m)
    tmp = bracket(n, m_2)
    if ans < tmp:
        ans = tmp
    for i in range(st, n):
        if m[i] == '+' or m[i] == '-':
            if m[i - 1] != ')' and m[i + 1] != '(':
                m.insert(i - 1, '(')
                m.insert(i + 3, ')')
                make_brack(n + 2, m, i + 2)
                m.pop(i + 3)
                m.pop(i - 1)
    return


N = int(input())
mathEx = list(input())

ans = -2 ** 31

make_brack(N, mathEx, 0)
print(ans)
