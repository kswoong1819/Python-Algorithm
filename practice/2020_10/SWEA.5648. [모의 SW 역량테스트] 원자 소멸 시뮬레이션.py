import sys

sys.stdin = open('input.txt')

dr = [0.5, -0.5, 0, 0]
dc = [0, 0, -0.5, 0.5]


# def move(atoms):
#     global result
#     dic = {}
#     for a in atoms:
#         a[0] += dc[a[2]]
#         a[1] += dr[a[2]]
#         try:
#             dic[(a[0], a[1])].append(a)
#         except:
#             dic[(a[0], a[1])] = [a]
#     atoms = []
#     for i in dic.keys():
#         if len(dic[i]) > 1:
#             for at in dic[i]:
#                 result += at[3]
#         else:
#             x = dic[i][0][0]
#             y = dic[i][0][1]
#             if -1000 <= x <= 1000 and -1000 <= y <= 1000:
#                 atoms.append(dic[i][0])
#     return atoms

def move(n, atoms):
    total = 0
    for i in range(4000):
        dic = {}
        for a in range(n):
            if atoms[a][3] != 0:
                atoms[a][1] += dr[atoms[a][2]]
                atoms[a][0] += dc[atoms[a][2]]
                nr, nc = atoms[a][1], atoms[a][0]
                if -1000 <= nr <= 1000 and -1000 <= nc <= 1000:
                    if (nr, nc) not in dic:
                        dic[nr, nc] = a
                    else:
                        total += atoms[a][3]
                        total += atoms[dic[nr, nc]][3]
                        atoms[dic[nr, nc]][3] = 0
                        atoms[a][3] = 0
    return total


T = int(input())
for t in range(T):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    result = move(N, atom)

    print('#{} {}'.format(t + 1, result))
