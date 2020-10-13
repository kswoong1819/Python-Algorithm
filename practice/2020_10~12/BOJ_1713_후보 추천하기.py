import sys

sys.stdin = open('input.txt')

N = int(input())
M = int(input())
students = list(map(int, input().split()))
frame = []
cnt = []
for s in students:
    if s in frame:
        tmp = frame.index(s)
        cnt[tmp] += 1
    else:
        if len(frame) >= N:
            tmp = cnt.index(min(cnt))
            frame.pop(tmp)
            cnt.pop(tmp)
        frame.append(s)
        cnt.append(1)

print(' '.join(map(str, sorted(frame))))
