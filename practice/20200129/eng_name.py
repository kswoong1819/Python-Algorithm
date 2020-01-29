names = input().split()

# list_m = []
# name = names[1:-1]
# for n in name:
#     m = n[0]+'.'
#     list_m.append(m)
# print(names[0], ' '.join(list_m), names[-1])

for i in range(1, len(names)-1):
    names[i] = names[i][0] + '.'
print(' '.join(names))