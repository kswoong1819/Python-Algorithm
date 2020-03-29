import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    