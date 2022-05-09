box = [7,4,2,0,0,6,0,7,0]

N = [0] * 10

for i in box:
    for j in range(1, i+1):
        N[j] += 1

min = 9877654
for k in range(10):
    if N[k] != 0 and N[k] < min:
        min = N[k]
print(len(box) - min)