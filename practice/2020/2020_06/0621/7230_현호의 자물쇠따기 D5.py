import sys

sys.stdin = open('input.txt')


def backtrack(k):
    if k == N:
        check(A)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        A.append(nums[i])
        backtrack(k + 1)
        A.pop()
        visited[i] = 0


def check(arr):
    global cnt
    num = ''.join(arr)
    if int(num) % K == 0:
        cnt += 1


result = []
T = int(input())
for t in range(T):
    N = int(input())
    nums = list(input().split())
    K = int(input())

    cnt = 0
    A = []
    visited = [0] * N
    backtrack(0)

    result.append([t + 1, cnt])

for idx, c in result:
    print('#{} {}'.format(idx, c))
