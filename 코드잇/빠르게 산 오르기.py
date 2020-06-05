def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    result = []
    dis = 0
    while dis < water_stops[-1]:
        dis += capacity
        while 1:
            if dis not in water_stops:
                dis -= 1
            else:
                result.append(dis)
                break

    return result


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))