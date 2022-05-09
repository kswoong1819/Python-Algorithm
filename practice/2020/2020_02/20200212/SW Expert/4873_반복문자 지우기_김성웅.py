T = int(input())

for t in range(T):
    words = input()
    stack = []

    for i in range(len(words)):
        if len(stack) == 0:
            stack.append(words[i])
        elif words[i] != stack[-1]:
            stack.append(words[i])
        else:
            stack.pop()
    print('#{} {}'.format(t+1,len(stack)))