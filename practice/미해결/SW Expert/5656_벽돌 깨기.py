import sys
sys.stdin = open('../../2020_03/20200304/input.txt')

T = int(input())

for t in range(T):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]


