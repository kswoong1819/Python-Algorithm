import sys
sys.stdin = open('input.txt')

def hungarian(mat):
    def Q(n, val=0): 
        return [val]*(n+1)
    n = len(mat)
    m = len(mat[0])
    u = Q(n)
    v = Q(m)
    p = Q(m)
    way = Q(m)
    for i in range(1, n+1):
        p[0] = i
        duplicate_check = 0
        minv = Q(m, float('inf'))
        used = Q(m, False)
        while p[duplicate_check]:
            used[duplicate_check] = True
            row = p[duplicate_check]
            delta = float('inf')
            select_col = None
            for j in range(1, m+1):
                if used[j]: continue
                cur = mat[row-1][j-1] - u[row] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = duplicate_check
                if minv[j] < delta:
                    delta = minv[j]
                    select_col = j
            for j in range(m+1):
                if used[j]:
                    u[p[j]]+= delta
                    v[j]-= delta
                else: minv[j]-= delta
            duplicate_check = select_col
        while duplicate_check: 
            select_col = way[duplicate_check]
            p[duplicate_check] = p[select_col]
            duplicate_check = select_col
    return -v[0]

n = int(input())
mat = [list(map(int,input().split())) for i in range(n)]
print(hungarian(mat))
