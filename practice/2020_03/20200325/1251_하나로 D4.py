import sys
sys.stdin = open('../20200324/input.txt')
import math

T = int(input())

for t in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    island = []
    for i in range(N):
        island.append([X[i], Y[i]])

    visited = [0] * N
    go(k)