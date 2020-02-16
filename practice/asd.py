def 회전(nums):
    tmp = [['']*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N-1-i] = nums[i][j]
    return tmp

def result(tmp, col):
    for i in range(N):
        for j in range(N):
            ans[i][col] += tmp[i][j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    ans = [['']*3 for _ in range(N)]

    for i in range(3):
        arr = 회전(arr)
        result(arr, i)

    print("#{}".format(tc))
    for i in range(N):
        for j in range(3):
            print(ans[i][j], end=" ")
        print()