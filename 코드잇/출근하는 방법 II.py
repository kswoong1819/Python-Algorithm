# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    if stairs < 2:
        return 1
    num = 0
    for i in possible_steps:
        if stairs >= i:
            num += staircase(stairs - i, possible_steps)
    return num

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))