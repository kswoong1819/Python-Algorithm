import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
N = int(input())
num = deque()
for i in range(N):
    word = input()
    if word[:4] == 'push':
        num.append(int(word[5:]))
    elif word[:3] == 'pop':
        if len(num) == 0:
            print('-1')
        else:
            print(num.popleft())
    elif word[:4] == 'size':
        print(len(num))
    elif word[:5] == 'empty':
        if len(num) == 0:
            print('1')
        else:
            print('0')
    elif word[:5] == 'front':
        if len(num) == 0:
            print('-1')
        else:
            print(num[0])
    elif word[:4] == 'back':
        if len(num) == 0:
            print('-1')
        else:
            print(num[-1])
