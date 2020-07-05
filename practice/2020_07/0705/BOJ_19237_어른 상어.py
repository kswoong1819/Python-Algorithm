import sys

sys.stdin = open('input.txt')

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


N, M, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
shark_dir = list(map(int, input().split()))
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

