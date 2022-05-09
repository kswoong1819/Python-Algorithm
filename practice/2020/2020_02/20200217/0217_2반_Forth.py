import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    list_ = input().split()
    stack = []

    print('#{} '.format(t+1), end='')
    for i in range(len(list_)):
        if list_[i].isdigit():
            stack.append(int(list_[i]))
        elif len(stack) >= 2:
            if list_[i] == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif list_[i] == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif list_[i] == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif list_[i] == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                print('error')
                break
        elif list_[i] == '.' and len(stack) == 1:
            result = stack.pop()
            print(result)
        else:
            print('error')
            break
