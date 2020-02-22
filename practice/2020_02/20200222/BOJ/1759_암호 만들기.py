import sys

sys.stdin = open('input.txt', 'r')


def go(k, start):
    if k == L:
        cnt_v = 0
        cnt_s = 0
        for x in A:
            if x in vowel:
                cnt_v += 1
            else:
                cnt_s += 1
        if cnt_v >= 1 and cnt_s >= 2:
            print(''.join(A))
        return
    for i in range(start, C):
        if check[i]:
            continue
        check[i] = True
        A.append(words[i])
        go(k + 1, i + 1)
        A.pop()
        check[i] = False


L, C = map(int, input().split())
words = input().split()
words.sort()

vowel = ['a', 'e', 'i', 'o', 'u']

A = []
check = [False] * C

go(0, 0)
