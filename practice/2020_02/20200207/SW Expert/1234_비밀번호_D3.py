import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    N, password = input().split()

    while 1:
        count = 0
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                password = password[:i] + password[i + 2:]
                count = 1
                break
        if count == 0:
            break

    print('#{} {}'.format(t+1, password))
