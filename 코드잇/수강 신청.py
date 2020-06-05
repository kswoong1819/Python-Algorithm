def course_selection(course_list):
    # 코드를 작성하세요.
    course_list.sort()
    N = len(course_list)
    max_ans = 0
    result = []

    for i in range(N):
        course = [course_list[i]]
        check = [0] * N
        check[i] = 1

        for x in range(1, N):
            for y in range(N):
                if check[y] == 0 and course[-1][1] <= course_list[y][0]:
                    course.append(course_list[y])
        tmp = len(course)
        if max_ans < tmp:
            max_ans = tmp
            result = course

    return result

# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
