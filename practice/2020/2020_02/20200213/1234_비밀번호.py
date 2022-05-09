import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    N, password = input().split()
    stack = []

    for i in range(int(N)):
        if len(stack) == 0:
            stack.append(password[i])
        elif password[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(password[i])

    print('#{} {}'.format(t+1,''.join(stack)))