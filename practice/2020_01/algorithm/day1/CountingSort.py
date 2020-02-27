data = [0,4,1,3,1,2,4,1]
B = [0]*len(data)
K = 4  # 자료의 최대값
cnt = [0]*(K+1)

for val in data:
    cnt[val] += 1
print(cnt)

# sorted = []
# for i in range(K+1):
#     for j in range(cnt[i]):
#         sorted.append(i)
# print(sorted)

for i in range(1, K+1):
    cnt[i] = cnt[i-1] + cnt[i]
print(cnt)

for j in range(len(data)-1, -1, -1):
    cnt[data[j]] -= 1
    B[cnt[data[j]]] = data[j]
print(B)