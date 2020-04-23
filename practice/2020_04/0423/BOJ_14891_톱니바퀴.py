import sys

sys.stdin = open('input.txt')
from collections import deque

def turn(num, dir):
    q = deque()
    rota_q = deque()
    q.append([num, dir])
    rota_q.append([num, dir])
    while q:
        n, d = q.popleft()
        visited[n] = 1
        if n == 1:
            if gear[n][2] != gear[n + 1][6] and visited[n+1]==0:
                q.append([n + 1, d * (-1)])
                rota_q.append([n + 1, d * (-1)])
        elif n == 4:
            if gear[n][6] != gear[n - 1][2] and visited[n-1]==0:
                q.append([n - 1, d * (-1)])
                rota_q.append([n - 1, d * (-1)])
        else:
            if visited[n + 1] == 0:
                if gear[n][2] != gear[n + 1][6]:
                    q.append([n + 1, d * (-1)])
                    rota_q.append([n + 1, d * (-1)])
            if visited[n - 1] == 0:
                if gear[n][6] != gear[n - 1][2]:
                    q.append([n - 1, d * (-1)])
                    rota_q.append([n - 1, d * (-1)])
    rotation(rota_q)


def rotation(rota):
    while rota:
        N, D = rota.popleft()
        if D == 1:
            tmp = gear[N].pop()
            gear[N] = [tmp] + gear[N]
        else:
            tmp = gear[N].pop(0)
            gear[N].append(tmp)


gear = [[]] + [list(map(int, input())) for _ in range(4)]
K = int(input())
for i in range(K):
    num, dir = map(int, input().split())
    visited = [0] * 5
    turn(num, dir)

ans = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        ans += 2**(i-1)

print(ans)