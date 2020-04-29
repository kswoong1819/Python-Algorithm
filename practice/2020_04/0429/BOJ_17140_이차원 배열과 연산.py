import sys
sys.stdin = open('input.txt')

def R_oper(matrix):
    k = [0] * 101
    for i in matrix:
        k[i] += 1
    A = []
    for i in range(1, max(k)+1):
        for j in range(1, 101):
            if k[j] == i:
                A.append(j)
                A.append(i)
    return A


# def C_oper():
#     for i in range(r):
#         k = [0] * 101
#         for j in range(c):
#             k[arr[j][i]] += 1
#         for i in range(1, max(k) + 1):
#             for j in range(1, 101):
#                 if k[j] == i:
#                     A.append(j)
#                     A.append(i)




r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

R, C = 3, 3

while arr[r][c] != k:
    if R >= C:
        for i in range(R):
            A = R_oper(arr[i])
            max_len = max(max_len, len(A))
            arr[i] = []
            arr[i] += A
        for i in range(R):
            tmp = max_len - len(arr[i])
            arr[i] += [0] * tmp

    # elif R < C:
    #     C_oper()
