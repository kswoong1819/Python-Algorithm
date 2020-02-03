import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    word = input()
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            print('#{} 0'.format(t+1))
            break
    else:
        print('#{} 1'.format(t + 1))