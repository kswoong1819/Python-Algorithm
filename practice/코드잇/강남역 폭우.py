def trapping_rain(buildings):
    # 코드를 작성하세요
    n = len(buildings)
    cnt = 0
    end = 0
    for i in range(n-1):
        st = ed = 0
        if i < end:
            continue
        if buildings[i] > 0:
            st = i
            for j in range(i+1, n):
                if buildings[i] <= buildings[j]:
                    ed = end = j
                    break
            else:
                continue
        tmp = 0
        for z in range(st+1, ed):
            tmp += buildings[z]
        cnt += buildings[st]*(ed-st-1) - tmp

    return cnt

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))