import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = input()
    people = list(map(int, input().split()))
    for i in people:
