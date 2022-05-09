import sys
sys.stdin = open('input.txt', 'r')

def pa_ch(n):
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False
    else:
        return True

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            word = []
            for k in range(j, j+M):
                word.append(matrix[i][k])
            if pa_ch(word):
                print('#{} '.format(t+1),end='')
                print(''.join(word))
                break

    for i in range(N-M+1):
        for j in range(N):
            word = []
            for k in range(i, i+M):
                word.append(matrix[k][j])
            if pa_ch(word):
                print('#{} '.format(t+1),end='')
                print(''.join(word))
                break