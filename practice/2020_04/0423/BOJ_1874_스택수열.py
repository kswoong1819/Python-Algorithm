import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []
stack = []
result = []
for i in range(N):
    num = int(input())
    arr.append(num)

idx = 0
for j in range(1, N + 1):
    stack.append(j)
    result.append('+')
    while idx < N and len(stack) != 0 and stack[-1] == arr[idx]:
        stack.pop()
        idx += 1
        result.append('-')

if len(stack):
    print('NO')
else:
    for i in result:
        print(i)
