import sys
sys.stdin = open('input.txt', 'r')

def cal(list_):
    stack = []
    for i in range(len(list_)):
        if list_[i].isdigit():
            stack.append(int(list_[i]))
        elif len(stack) >= 2:
            if list_[i] == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif list_[i] == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
    result = stack.pop()
    return result

for t in range(10):
    length = int(input())
    math = input()
    stack = []
    num_list = []

    icp = {'*': 2, '+': 1, '(': 3}
    isp = {'*': 2, '+': 1, '(': 0}

    for i in range(length):
        if math[i].isdigit():
            num_list.append(math[i])
        else:
            if len(stack) == 0:
                stack.append(math[i])
                continue
            elif len(stack) > 0:
                if math[i] == ')':
                    while stack[-1] != '(':
                        num_list.append(stack.pop())
                    stack.pop()

                elif icp[math[i]] > isp[stack[-1]]:
                    stack.append(math[i])
                else:
                    while icp[math[i]] <= isp[stack[-1]]:
                        num_list.append(stack.pop())
                    stack.append(math[i])

    print('#{} {}'.format(t+1,cal(num_list)))