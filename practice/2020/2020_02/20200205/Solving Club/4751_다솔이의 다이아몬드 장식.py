import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    word = input()
    n = len(word)
    print('..#.'*n + '.')
    print('.#'*n*2 + '.')
    for i in word:
        print('#.{}.'.format(i), end='')
    print('#')
    print('.#'*n*2 + '.')
    print('..#.'*n + '.')