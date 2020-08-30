def solution(v):
    x = []
    y = []
    for i in range(3):
        a, b = v[i]
        if a not in x:
            x.append(a)
        else:
            x.remove(a)
        if b not in y:
            x.append(b)
        else:
            x.remove(b)

    answer = x + y

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))