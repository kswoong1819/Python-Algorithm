# import sys
# sys.stdin = open('input.txt', 'r')

for t in range(10):
    T = int(input())
    st = input()
    word = input()

    tmp = word.count(st)
    print('#{} {}'.format(t+1, tmp))