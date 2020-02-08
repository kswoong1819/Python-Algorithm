import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    words = [[i for i in input()] for _ in range(5)]
    max_len = 0
    for x in range(5):
        if max_len < len(words[x]):
            max_len = len(words[x])
    arr = [[0] * max_len for _ in range(5)]

    for i in range(5):
        for j in range(len(words[i])):
            arr[i][j] = words[i][j]

    print('#{} '.format(t + 1), end='')
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] != 0:
                print(arr[j][i], end='')
    print()
