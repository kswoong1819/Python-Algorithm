import sys
sys.stdin = open('input.txt')

def go(n, total):
    


N = int(input())
population = list(map(int, input().split()))
area = [[0]*(N+1) for _ in range(N+1)]
for n in range(1, N+1):
    contact = list(map(int, input().split()))
    for i in range(1, contact[0]+1):
        area[n][contact[i]] = 1

for i in range(1, N+1):
    go([i], population[i])