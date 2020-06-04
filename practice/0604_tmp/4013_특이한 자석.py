import sys

sys.stdin = open('input.txt')


def rotation(mag, d):
    if d == 1:
        tmp = mag.pop()
        mag.insert(0, tmp)
    if d == -1:
        tmp = mag.pop(0)
        mag.append(tmp)


def go(num, dir):
    go_rotation = [[num, dir]]
    n, r = num, dir
    while n < 3:
        if magnatic[n][2] != magnatic[n + 1][6]:
            n += 1
            r *= -1
            go_rotation.append([n, r])
        else:
            break

    n, r = num, dir
    while n > 0:
        if magnatic[n][6] != magnatic[n - 1][2]:
            n -= 1
            r *= -1
            go_rotation.append([n, r])
        else:
            break

    for idx, d in go_rotation:
        rotation(magnatic[idx], d)


T = int(input())

for t in range(T):
    K = int(input())
    magnatic = [list(map(int, input().split())) for _ in range(4)]
    for i in range(K):
        num, rot = map(int, input().split())
        go(num - 1, rot)

    result = 0
    for i in range(4):
        if magnatic[i][0] == 1:
            result += 2 ** i

    print('#{} {}'.format(t + 1, result))
