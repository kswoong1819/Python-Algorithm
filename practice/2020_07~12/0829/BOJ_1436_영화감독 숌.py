import sys
sys.stdin = open('input.txt')

N = int(input())
st = 666
cnt = 1

while 1:
    if N == cnt:
        break
    while 1:
        st += 1
        if '666' in str(st):
            cnt += 1
            break

print(st)
