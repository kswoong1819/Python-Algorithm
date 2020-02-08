import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    pair = int(input())
    screw = input().split()
    pair_list = [[screw[x] for x in range(y, y+2)] for y in range(0, len(screw), 2)]

    for y in pair_list:
        ans = []
        n = 0
        ans.append(y)
        while len(ans) != pair:
            for i in pair_list:
                if ans[n][1] == i[0]:
                    ans.append(i)
                    n += 1
                    break
            else:
                break

        if len(ans) == pair:
            break

    print('#{} '.format(t + 1), end='')
    for x in ans:
        print(' '.join(x), end=' ')
    print()