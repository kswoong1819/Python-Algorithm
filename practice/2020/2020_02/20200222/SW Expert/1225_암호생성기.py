import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    T = int(input())
    password = list(map(int, input().split()))
    val = 1

    while 1:
        tmp = password.pop(0) - val
        password.append(tmp)
        val += 1
        if val > 5:
            val = 1
        if password[-1] <= 0:
            password[-1] = 0
            break

    print('#{} '.format(T), end='')
    for i in range(8):
       print(password[i], end=' ')
    print()