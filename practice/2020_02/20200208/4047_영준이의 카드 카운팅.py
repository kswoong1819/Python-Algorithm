import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
pattern = {'S':0, 'D':1, 'H':2, 'C':3}

for t in range(T):
    card = input()
    arr = [[0]*14 for _ in range(4)]

    for i in range(0, len(card), 3):
        flag = True
        r = pattern[card[i]]
        c = int(card[i+1:i+3])
        if arr[r][c] == 1:
            flag = False
            break
        arr[r][c] = 1
        arr[r][0] += 1

    print('#{} '.format(t+1),end='')
    if flag:
        for i in range(4):
            print(13 - arr[i][0],end=' ')
        print()
    else:
        print('ERROR')


