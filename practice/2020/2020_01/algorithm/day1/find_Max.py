# 최대값 찾기
arr2=[55,7,78,12,42]
findmax=arr2[0]
for i in range(1,len(arr2)):
    if findmax<arr2[i]:
        findmax=arr2[i]
print(findmax)

# 최대값 인덱스 찾기
arr = [55,7,78,12,42]
idx = 0
for i in range(1, len(arr)):
    if arr[idx] < arr[i]:
        idx = i
print(idx, arr[idx])