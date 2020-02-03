# def factorial(a):
#     result = 1
#     while a>0:
#         result *= a
#         a -= 1
#     return result

# num = int(input())
# print(factorial(num))

# 재귀함수
def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a-1)

num = int(input())
print(factorial(num))