import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    word = input()
    if len(word) % 2:
        print('#{} {}'.format(t + 1, 'Not exist'))
    else:
        for i in range(len(word) // 2):
            if word[i] != word[-1 - i]:
                print('#{} {}'.format(t + 1, 'Not exist'))
                break
        else:
            print('#{} {}'.format(t + 1, 'Exist'))
