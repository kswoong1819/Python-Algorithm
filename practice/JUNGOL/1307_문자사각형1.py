N = int(input())

'''
alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
arr = [[alpa[i % 26] for i in range(j, j+N)] for j in range(0, N*N, N)]
''' # 문자열사용

arr = [[chr((i%26) + 65) for i in range(j, j+N)] for j in range(0, N*N, N)]
# chr()  유니코드 --> 문자
# ord()  문자  --> 유니코드
# ord('A') = 65
# ((i%26) + 65) 의미 --> A, Z까지 이후 다시 A부터 시작

for i in range(N):
    for j in range(N):
        print(arr[-j-1][-i-1], end=' ')
    print()