import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    word_1 = input()
    word_2 = input()

    result = 0
    for i in word_1:
        tmp = word_2.count(i)
        if result < tmp:
            result = tmp

    print('#{} {}'.format(t+1, result))