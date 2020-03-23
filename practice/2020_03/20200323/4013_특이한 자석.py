import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    K = int(input())
    magnetic = [input().split() for _ in range(4)]
    rota = [input().split() for _ in range(K)]
    score = [1, 2, 4, 8]

    for i in range(K):
        rota[0][0]