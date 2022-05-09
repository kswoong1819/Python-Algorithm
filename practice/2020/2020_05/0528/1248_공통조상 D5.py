import sys

sys.stdin = open('input.txt')
from collections import deque


def find_top():
    A = [x]
    B = [y]
    while 1:
        nxt_x = tree_pa[A[-1]][0]
        A.append(nxt_x)
        if nxt_x == 1:
            break
    while 1:
        nxt_y = tree_pa[B[-1]][0]
        B.append(nxt_y)
        if nxt_y in A:
            return nxt_y


def find_cnt(st):
    q = deque()
    q.append(st)
    cnt = 1
    while q:
        n = q.popleft()
        for i in tree_ch[n]:
            cnt += 1
            q.append(i)
    return cnt


T = int(input())

for t in range(T):
    V, E, x, y = map(int, input().split())
    lines = list(map(int, input().split()))
    tree_pa = [[] for _ in range(V + 1)]
    tree_ch = [[] for _ in range(V + 1)]
    for i in range(0, E * 2, 2):
        tree_pa[lines[i + 1]].append(lines[i])
        tree_ch[lines[i]].append(lines[i + 1])

    top = find_top()
    cnt = find_cnt(top)

    print('#{} {} {}'.format(t + 1, top, cnt))
