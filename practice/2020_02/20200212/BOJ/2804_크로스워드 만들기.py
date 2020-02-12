import sys
sys.stdin = open('input.txt', 'r')

def cross_point(n,m):
    for i in range(len(n)):
        for j in range(len(m)):
            if n[i] == m[j]:
                return i, j

A, B = input().split()

matrix = [['.']*len(A) for _ in range(len(B))]

point = cross_point(A, B)

for i in range(len(A)):
    for j in range(len(B)):
        matrix[point[1]][i] = A[i]
        matrix[j][point[0]] = B[j]

for i in range(len(B)):
    print(''.join(matrix[i]))
