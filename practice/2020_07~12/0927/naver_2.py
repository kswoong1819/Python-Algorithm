block = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
L = len(block)
result_L = sum([i for i in range(L + 1)])
answer = []
arr = [[200] * L for _ in range(L)]
for i in range(len(block)):
    arr[i][block[i][0]] = block[i][1]
    result_L -= 1
while result_L != 0:
    for i in range(4):
        for j in range(i+1):
            if arr[i][j] == 200 and arr[i+1][j] != 200 and arr[i+1][j+1] != 200:
                arr[i][j] = arr[i+1][j] + arr[i+1][j+1]
                result_L -= 1
            elif arr[i][j] != 200 and arr[i+1][j] == 200 and arr[i+1][j+1] != 200:
                arr[i+1][j] = arr[i][j] - arr[i+1][j+1]
                result_L -= 1
            elif arr[i][j] != 200 and arr[i+1][j] !=200 and arr[i+1][j+1] == 200:
                arr[i+1][j+1] = arr[i][j] - arr[i+1][j]
                result_L -= 1

for i in range(5):
    for j in range(i+1):
        answer.append(arr[i][j])

for a in arr:
    print(a)

print(answer)