import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
B, C = map(int, input().split())

total = N
for i in range(N):
    people[i] -= B
    if people[i] < 0:
        people[i] = 0
    tmp = people[i] // C
    if people[i] % C:
        total += tmp + 1
    else:
        total += tmp

print(total)