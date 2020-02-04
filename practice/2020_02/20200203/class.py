## 2020_02_03

# import sys
# sys.stdin = open('input.txt', 'r')

'''
# R,C = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(R)]
# arr2 = [[0]*C for _ in range(R)]

# 행 우선 순회
# for i in range(R):
#     for j in range(C):
#         arr2[i][j] = arr[i][j]
#         print(arr[i][j], end=' ')
# print()
# print(arr2)


# 열 우선 순회
# for i in range(C):
#     for j in range(R):
#         print(arr[j][i], end='')


# 행을 뒤에서부터 출력
# for i in range(R):
#     for j in range(C):
#         print(arr[i][-j-1], end='')

# 열을 밑에서 부터 출력
# for j in range(C):
#     for i in range(R):
#         print(arr[-i-1][j], end='')

# 지그재그 행
# for i in range(R):
#     for j in range(C):
#         print(arr[i][j + (-j-1-j)*(i%2)], end=' ')


# 지그재그 열
# for j in range(C):
#     for i in range(R):
#         print(arr[i + (-i-1-i)*(j%2)][j], end=' ')
'''# 행렬 출력

'''
# 상하좌우 델타
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]     # drc = [[-1,0],[1,0],[0,-1],[0,1]]
# 
# r = 1
# c = 1
# 
# R,C = map(int, input().split())
# arr = [input().split() for _ in range(R)]
# 
# for k in range(4):
#     nr = r + dr[k]
#     nc = c + dc[k]
#     if nr >= 0 and nr < R and nc >= 0 and nc < C:   # 0 <= nr < R and 0 <= nc < C
#         print(arr[nr][nc])
'''# 상하좌우 델타

'''
#1. 1~25까지 증가하면서 5 5 크기의 배열에 입력
arr = [[0 for _ in range(5)] for _ in range(5)]
num=1
for i in range(5):
    for j in range(5):
        arr[i][j]+=num
        num+=1
    print(arr[i])

#2. 이웃한 요소가 홀수 일때만 더한 값을 출력하기
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for i in range(5):
    for j in range(5):
        sum=0
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if arr[ny][nx]%2!=0:
                    sum += arr[ny][nx]
        print(sum)

#3. 절대값의 합의 차
def m_abs(num):
    if num <0:
        return -num
    return num
for i in range(5):
    for j in range(5):
        sum=0
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < 5 and 0 <= nx < 5:
                sum+= m_abs(arr[ny][nx]-arr[i][j])
        print(sum)

#4. 대각 요소 4군데 접근해 합을 구하고 그 합중 가장 큰 값을 출력
dy2 = [-1,-1,1,1]
dx2 = [-1,1,-1,1]
max_value = 0
for i in range(5):
    for j in range(5):
        sum2 = 0
        for k in range(4):
            ny2 = i+dy2[k]
            nx2 = i+dx2[k]
            if 0 <= ny2 < 5 and 0 <= nx2 < 5:
                sum2 += arr[ny2][nx2]
        if sum2 > max_value:
            max_value = sum2
print(max_value)
'''#연습문제 1

'''
# 부분집합
word = ['단무지', '햄', '참치', '돈까스']

bit = [0,0,0,0]

for a in range(2):
    bit[0] = a
    for b in range(2):
        bit[1] = b
        for c in range(2):
            bit[2] = c
            for d in range(2):
                bit[3] = d
                print(bit)
                for i in range(len(bit)):
                    if bit[i] == 1:
                        print(word[i], end=' ')
                print('이 들어간 김밥')
'''# 부분집합

'''
# 2진수 만들기
# 127 256 19
# N = [127, 256, 19]
# for n in N:
#     num_list = []
#     while n > 0:
#         num = n % 2
#         num_list.append(num)
#         n //= 2
#     for i in range(len(num_list)):
#         print(num_list[-i-1], end='')
#     print()

#십진수로 만들기
# 11011 100111 1111
'''# 2진수 만들기

'''
# 부분집합 비트연산
word = ['단무지', '햄', '참치', '돈까스']

N = len(word)

for i in range(1<<N):
    for j in range(N):
        if i & (1<<j):
            print(word[j], end=' ')
    print('김밥입니다.')
'''# 부분집합 비트연산

'''
# 연습문제 2
# 1 2 3 4 5 6 7 8 9 10 이 주어졌을때 부분집합의 합이 11되는 경우를 모두 출력하시오.

arr = [x for x in range(1,11)]
n = len(arr)

for i in range(1<<n):
    subset_sum = 0
    subset_list = []
    for j in range(n):
        if i & (1<<j):
            subset_sum += arr[j]
            subset_list.append(arr[j])
    if subset_sum == 11:
        print(subset_list)
'''# 연습문제 2

'''
# 순차 검색

# 4 9 11 23 2 19 7 를 가진 리스트를 선언을 하고
# 1. 11을 찾을때 걸리는 횟수와 과정을 출력
# 2. 10을 찾을때 걸리는 횟수와 과정을 출력

# N = [4,9,11,23,2,19,7]
#
# count = 0
# for i in range(len(N)):
#     count += 1
#     if N[i] == 11:
#         break
# print(count)

# number_list = [4,9,11,23,2,19,7]
# number_list = sorted(number_list)
# key =11
# cnt = 0
# flag = False
# for i in range(len(number_list)):
#     cnt+=1
#     print(number_list[i],'와',key,'를 비교한다.')
#     if number_list[i] > key:
#         break
#     if number_list[i] == key:
#         flag = True
#         break
# if flag:
#     print(cnt,'찾음')
# else:
#     print(cnt,'못찾음')

# 위의 리스트를 정렬하고
# 1. 11을 찾을때 걸리는 횟수와 과정을 출력
# 2. 10을 찾을때 걸리는 횟수와 과정을 출력

# def bubblesort(a):
#     for i in range(len(a)-1, 0,-1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
# 
# number_list = [4,9,11,23,2,19,7]
# number_list = sorted(number_list)
# key =11
# cnt = 0
# flag = False
# for i in range(len(number_list)):
#     cnt+=1
#     print(number_list[i],'와',key,'를 비교한다.')
#     if number_list[i] > key:
#         break
#     if number_list[i] == key:
#         flag = True
#         break
# if flag:
#     print(cnt,'찾음')
# else:
#     print(cnt,'못찾음')
'''# 순차 검색
