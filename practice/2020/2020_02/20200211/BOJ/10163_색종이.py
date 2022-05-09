import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
matrix = [[0]*101 for _ in range(101)]
for n in range(1,N+1):
    r1,c1,r2,c2 = map(int, input().split())
    for i in range(r1, r1+r2):
        for j in range(c1, c1+c2):
            matrix[i][j] = n


for x in range(1,N+1):
    result = 0
    for y in range(101):
        result += matrix[y].count(x)
    print(result)
