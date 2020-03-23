import sys

sys.stdin = open('../../2020_03/20200323/input.txt')


def turn_left(n):
    tmp = n.pop(0)
    n.append(tmp)
    return n


def turn_right(n):
    tmp = [n.pop()]
    tmp.extend(n)
    return tmp

def rotation(x):
    if rota[x][1] > 0:
        turn_right(magnetic[rota[x][0] - 1])
        turn_left(magnetic[rota[x][0]])
    else:
        turn_right(magnetic[rota[x][0]])
        turn_left(magnetic[rota[x][0] - 1])


T = int(input())

for t in range(T):
    K = int(input())
    magnetic = [input().split() for _ in range(4)]
    rota = [list(map(int, input().split())) for _ in range(K)]
    score = [1, 2, 4, 8]

    for i in range(K):
        if magnetic[rota[i][0]] == '1':
            if magnetic[rota[i][0] - 1][2] != magnetic[rota[i][0]][-2]:
                rotation(i)
            else:
                if rota[i][1] > 0:
                    turn_right(magnetic[rota[i][0] - 1])
                else:
                    turn_left(magnetic[rota[i][0] - 1])
