def solution(t1, t2):
    answer = -1
    for n in t1:
        lst = [[n, t2[0]]]
        while lst:
            a, b = lst.pop()
            for i in range(2):
                check(a[i], b[i])
    return answer

def check(a, b):
    if a > 0 and b > 0:
        return [a, b]
    elif a > 0 and b < 0:
        return False
    elif a < 0 and b > 0:



t1 = [[1, 2], [3, 4], [5, 6], [-1, 7], [8, 9], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
t2 = [[1, 2], [-1, -1], [-1, -1]]
print(solution(t1, t2))
