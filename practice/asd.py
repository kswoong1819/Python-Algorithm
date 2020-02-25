def binary_search(element, some_list):
    # 코드를 작성하세요.
    st = 0
    ed = len(some_list) - 1
    while st <= ed:
        center = (st + ed) // 2
        if element == some_list[center]:
            return center
        elif element > some_list[center]:
            st = center + 1
        elif element < some_list[center]:
            ed = center - 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))