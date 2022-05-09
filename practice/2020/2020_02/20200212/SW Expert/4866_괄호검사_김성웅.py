T = int(input())

for t in range(T):
    word = input()
    stack = []
    brack_left = ['(', '{']
    flag = True
    for i in word:
        if i in brack_left:
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                flag = False
                break
            tmp = stack.pop()
            if '(' != tmp:
                flag = False
                break
        if i == '}':
            if len(stack) == 0:
                flag = False
                break
            tmp = stack.pop()
            if '{' != tmp:
                flag = False
                break

    if len(stack) == 0 and flag == True:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))