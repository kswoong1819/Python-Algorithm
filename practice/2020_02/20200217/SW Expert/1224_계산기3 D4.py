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
        elif len(stack) == 1:
            return stack.pop()

for t in range(1):
    N = int(input())
    list_ = input()

    isp = {'*': 4, '/': 4, '+': 2, '-': 2, '(': 1, ')':50}
    icp = {'*': 4, '/': 4, '+': 2, '-': 2, '(': 5, ')':0}

    stack = []
    oper = []
    for i in list_:
        if i.isdigit():
            stack.append(i)
        else:
            if len(oper) == 0:
                oper.append(i)
            elif icp[i] > isp[oper[-1]]:
                oper.append(i)
            elif icp[i] < isp[oper[-1]]:
                tmp = oper.pop()
                if tmp == '(':
                    continue
                stack.append(tmp)
                if oper[len(oper)-1:] == '(':
                    oper.pop()
            elif icp[i] == isp[oper[-1]]:
                tmp = oper.pop()
                stack.append(tmp)
                oper.append(i)
    while len(oper) != 0:
        if oper[-1] == '(':
            oper.pop()
        else:
            tmp = oper.pop()
            stack.append(tmp)

    print(cal(stack))