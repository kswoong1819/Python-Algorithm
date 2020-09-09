def solution(p):
    if len(p) == 0 or check(p):
        return p
    tmp = separate(p) + 1
    u = p[:tmp]
    v = p[tmp:]
    if check(u):
        string = solution(v)
        return u + string
    else:
        t = "("
        t += solution(v)
        t += ")"
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        t += "".join(u)
        return t


def check(arr):
    stack = []
    for i in arr:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True


def separate(arr):
    tmp = 0
    for i in range(len(arr)):
        if arr[i] == "(":
            tmp += 1
        else:
            tmp -= 1
        if tmp == 0:
            return i


# p = "(()())()"
# p = ")("
# p = "()))((()"
# p = "))()))(((("
p = ")()()()("
print(solution(p))
