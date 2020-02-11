import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]

nation.sort()

count = 1
for i in range(N):
    if nation[i][1] > nation[K-1][1]:
        count += 1
    if nation[i][1] == nation[K-1][1]:
        if nation[i][2] > nation[K-1][2]:
            count += 1
        if nation[i][2] == nation[K-1][2]:
            if nation[i][3] > nation[K-1][3]:
                count += 1
print(count)