import sys
sys.stdin = open('input.txt', 'r')


for t in range(10):
    N = int(input())
    password = list(map(int, input().split()))
    M = int(input())
    command = input().split()

    for i in range(len(command)):
        if command[i] == 'I':
            for j in range(int(command[i+2])-1,-1,-1):
                password.insert(int(command[i+1]), command[i+3+j])
        if command[i] == 'D':
            del password[int(command[i+1]):int(command[i+1])+int(command[i+2])]
        if command[i] == 'A':
            for j in range(int(command[i+1])):
                password.append(command[i+2+j])

    print('#{}'.format(t+1), end=' ')
    for x in range(10):
        print(password[x], end=' ')
    print()
