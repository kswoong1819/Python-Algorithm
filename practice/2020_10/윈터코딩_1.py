def solution(n, delivery):
    answer = ''
    delivery.sort(key=lambda x: x[2], reverse=True)
    arr = [0] * (n + 1)
    for a, b, c in delivery:
        if c == 1:
            arr[a] = 1
            arr[b] = 1
        else:
            if arr[a] == 1 or arr[b] == 1:
                if arr[b] == 1:
                    arr[a] = 2
                else:
                    arr[b] = 2
    for i in range(1, n + 1):
        if arr[i] == 0:
            answer += '?'
        elif arr[i] == 1:
            answer += 'O'
        else:
            answer += 'X'
    return answer


n = 7
delivery = [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]
print(solution(n, delivery))
