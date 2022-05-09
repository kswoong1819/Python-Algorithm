def my_max(arr):
    num=arr[0]
    for i in range(1, len(arr)):
        if num < arr[i]:
            num = arr[i]
    return num

def my_min(arr):
    num=arr[0]
    for i in range(1, len(arr)):
        if num > arr[i]:
            num = arr[i]
    return num

TC = int(input())
for i in range(1,TC+1):
    N = int(input())
    num = list(map(int,input().split()))
    result = my_max(num) - my_min(num)
    print(f'#{i} {result}')