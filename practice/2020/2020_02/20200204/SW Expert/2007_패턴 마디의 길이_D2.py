import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    words = input()
    word = ''
    count = 0

    for i in range(2):
        word += words[i]

    for x in range(1, len(words)-1):
        check_word = ''
        for i in range(2):
            check_word += words[i+x]
        if word == check_word:
            break
    print('#{} {}'.format(t+1,x))