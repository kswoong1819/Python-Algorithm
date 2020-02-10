import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    word_1 = input()
    word_2 = input()

    if word_1 in word_2:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))