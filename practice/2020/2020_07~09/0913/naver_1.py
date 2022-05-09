def solution(boxes):
    L = len(boxes)
    product = {}
    for p in boxes:
        for i in range(2):
            if p[i] not in product:
                product[p[i]] = 1
            else:
                product[p[i]] += 1
    even = 0
    for i in product:
        even += product[i] // 2
    answer = L - even
    return answer


# boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
boxes = [[1, 2], [3, 4], [5, 6]]
# boxes = [[2, 2], [2, 2], [1, 1]]
print(solution(boxes))
