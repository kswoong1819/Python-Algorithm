import sys
sys.stdin = open('input.txt', 'r')

def make_bar(n):
    con = [screw[n]]
    use = [0] * N
    use[n] = 1
    for i in range(N-1):
        isok = True
        for j in range(N):
            if use[j] != 1 and con[i][1] == screw[j][0]:
                con.append(screw[j])
                use[j] = 1
                isok = False
                break
        if isok:
            break
    return con


T = int(input())

for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    screw = []
    for i in range(0, len(num_list), 2):
        screw.append([num_list[i], num_list[i+1]])

    ans = []
    for i in range(N):
        tmp = make_bar(i)
        if len(ans) < len(tmp):
            ans = tmp

    print('#{} '.format(t+1),end='')
    for i in range(N):
        print('{} {}'.format(ans[i][0], ans[i][1]), end = ' ')
    print()