import sys
sys.stdin = open('input.txt', 'r')

def palin(ch_list):
    for i in range(len(ch_list)//2):
        if ch_list[i] != ch_list[-i-1]:
            return False
    return True

for t in range(1):
    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8-N+1):
            ch_list = []
            for k in range(j, j+N):
                ch_list.append(matrix[i][k])
            if palin(ch_list):
                count += 1

    for i in range(8-N+1):
        for j in range(8):
            ch_list = []
            for k in range(i, i+N):
                ch_list.append(matrix[k][j])
            if palin(ch_list):
                count += 1

    print('#{} {}'.format(t+1, count))