import sys
sys.stdin = open('../../2020_03/20200315/input.txt')

def go(k):
    if k == K:
        find(A)
        return
    for i in range(1, K+1):
        if arr[i]:
            continue
        A.append(i)
        arr[i] = 1
        go(k+1)
        A.pop()
        arr[i] = 0

def find(A):
    global min_cnt, min_ls
    result = []
    cnt = 0
    ls = []
    for i in A:
        ls += [i]*check[i]
    for x in range(len(ls)):
        if ls[x] != nums[x]:
            cnt += 1
            result.append([ls[x], nums[x]])
    if min_cnt > cnt:
        min_cnt = cnt
        min_ls = result


N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

check = [0] * (K+1)
for i in nums:
    check[i] += 1

arr = [0] * (K+1)
A = []
min_ls = []
min_cnt = 987654321
go(0)

ans = 0
for i in range(min_cnt-1):
    if min_ls[i] == 0:
        continue
    for j in range(i, min_cnt):
        if min_ls[i] == 0:
            continue
        if [min_ls[i][1], min_ls[i][0]] == min_ls[j]:
            ans += 1
            min_ls[i] = min_ls[j] = 0
            break
if min_cnt - ans*2 > 0:
    tmp = min_cnt - ans*2
    ans += tmp - 1
print(ans)
