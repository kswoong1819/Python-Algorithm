import sys
sys.stdin = open('input.txt', 'r')

def find_idx(n):
    idx = 0
    for i in range(len(n)):
        if n[i] > n[idx]:
            idx = i
    return idx

T = int(input())

for t in range(T):
    N = int(input())
    time = list(map(int, input().split()))

    result = 0
    while 1:
        tmp = find_idx(time)
        sum = 0
        for i in range(tmp):
            sum += time[i]
        result += time[tmp]*tmp - sum
        time = time[tmp+1:]
        if len(time) == 0 or time[tmp] < time[-1]:
            break

    print(result)
