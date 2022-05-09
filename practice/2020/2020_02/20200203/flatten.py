def min_search():
    minValue = 987654321
    min_idx = -1
    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i
    return min_idx

def max_search():
    maxValue = 987654321
    max_idx = -1
    for i in range(len(box)):
        if box[i] < max_value:
            max_value = box[i]
            max_idx = i
    return max_idx

for tc in range(1,11):
    N = int(input())

    box = map(int, input().split())

    for i in range(N):
        box[max_search]
        box[min_search]

        box[maxIdx] -= 1
        box[minIdx] += 1

