# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기 코드를 쓰세요
    minDis = 987654321
    ans_i = ans_j = 0
    n = len(coordinates)
    for i in range(n-1):
        for j in range(i+1, n):
            tmp = distance(coordinates[i], coordinates[j])
            if minDis > tmp:
                minDis = tmp
                ans_i = coordinates[i]
                ans_j = coordinates[j]
    return [ans_i, ans_j]
# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))