# def fibo(a):
#     fibo_list = [1] * a
#     for i in range(1,a-1):
#         fibo_list[i+1] = fibo_list[i-1] + fibo_list[i]
#     return fibo_list

# num = int(input())
# print(fibo(num))

# 재귀함수
def fibo(a):
    if a<2:
        return a
    return fibo(a-1)+fibo(a-2)

num = int(input())
print(fibo(num))