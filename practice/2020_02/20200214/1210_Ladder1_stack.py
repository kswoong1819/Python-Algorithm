import sys
sys.stdin = open('input.txt', 'r')



for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

