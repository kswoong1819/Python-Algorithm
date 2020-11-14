import sys
sys.stdin = open('input.txt')


def track(k, st):
    if k == att:
        check(nums)
        return
    for i in range(st, 6):
        nums.append(i)
        track(k+1, i+1)
        nums.pop()

def check(arr):
    ch = {}
    for i in range(numofrow):
        tmp = []
        for j in arr:
            tmp.append(data[i][j])
        tmp.sort()
        pattern = ",".join(tmp)
        if pattern in ch:
            ch[pattern] += 1
        else:
            ch[pattern] = 1
    for key, value in ch.items():
        if value >= thres * numofrow:
            print(key)

att = int(input())
thres = float(input())
numofrow = int(input())
data = [sys.stdin.readline()[:-1].split(',') for _ in range(numofrow)]


nums = []
track(0, 0)
# ch2 = sorted(ch.items(), reverse=True, key=lambda item: item[0])
# print(ch2)
