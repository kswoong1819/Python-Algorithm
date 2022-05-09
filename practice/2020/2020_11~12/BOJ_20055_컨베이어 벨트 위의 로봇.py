import sys

sys.stdin = open('input.txt')


def rota(n_arr):
    ed = n_arr[:-1]
    st = n_arr[-1:]
    return st + ed


def robot_move(arr, robot):
    global K_cnt
    for i in range(N - 2, -1, -1):
        if robot[i] == 1 and arr[i] == 0:
            robot[i] = 0
        elif robot[i] == 1 and robot[i + 1] == 0 and arr[i + 1] != 0:
            arr[i + 1] -= 1
            robot[i] = 0
            if arr[i + 1] == 0:
                K_cnt += 1
                continue
            if i + 1 == N - 1:
                continue
            robot[i + 1] = 1


N, K = map(int, input().split())
arr = list(map(int, input().split()))
robot = [0] * N

K_cnt = 0
result = 0
while K_cnt < K:
    result += 1
    arr = rota(arr)
    robot_move(arr, robot)
    if robot[0] == 0 and arr[0] > 0:
        arr[0] -= 1
        if arr[0] == 0:
            K_cnt += 1
            continue
        robot[0] = 1

print(result)
