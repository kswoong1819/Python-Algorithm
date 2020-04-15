import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def cal(k, cur):
    global ans_min, ans_max
    if k == N-1:
        ans_min = min(ans_min, cur)
        ans_max = max(ans_max, cur)
        return
    if oper[0] != 0:
        oper[0] -= 1
        cal(k+1, cur + nums[k+1])
        oper[0] += 1
    if oper[1] != 0:
        oper[1] -= 1
        cal(k+1, cur - nums[k+1])
        oper[1] += 1
    if oper[2] != 0:
        oper[2] -= 1
        cal(k+1, cur * nums[k+1])
        oper[2] += 1
    if oper[3] != 0:
        oper[3] -= 1
        if cur < 0:
            cal(k+1, -(abs(cur) // nums[k+1]))
        else:
            cal(k+1, cur // nums[k+1])
        oper[3] += 1


N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))


ans_max = -float('inf')
ans_min = float('inf')
cal(0, nums[0])

print(ans_max)
print(ans_min)