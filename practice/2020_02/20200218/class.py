# arr = 'ABC'
# N = len(arr)
# visit = [0] * N         # 이전에 선택한 요소들에 대한 정보
# order = []
#
# def backtrack(k):       # k: 함수 호출에서 높이, 선택한 요소의 수
#     if k == N:          # 단말노드의 도착, 모든 선택이 끝났다.
#         print(order)    # order에 하나의 순열이 저장된 상태
#     else:               # 아직 해야할 선택이 남은 상태
#         for i in range(N):
#             if visit[i]:
#                 continue
#             visit[i] = 1
#             order.append(arr[i])
#             backtrack(k+1)
#             order.pop()
#             visit[i] = 0
#
# backtrack(0)


# arr = [i for i in range(1, 11)]
# N = len(arr)
#
# # bit = [0] * N
# #
# # def backtrack(k):
# #     if k == N:
# #         S = 0
# #         for i in range(N):
# #             if bit[i]:
# #                 S += arr[i]
# #         if S == 10:
# #             for i in range(N):
# #                 if bit[i]:
# #                     print(arr[i], end=' ')
# #             print()
# #
# #
# #     else:
# #         bit[k] = 1
# #         backtrack(k+1)  # k번 요소를 포함
# #         bit[k] = 0
# #         backtrack(k+1)  # k번 요소를 포함하지 않음
# #
# # backtrack(0)
#
# # A = []
# # def backtrack(k):
# #     if k == N:
# #         if sum(A) == 10:
# #             print(A)
# #
# #     else:
# #         A.append(arr[k])
# #         backtrack(k + 1)  # k번 요소를 포함
# #         A.pop()
# #         backtrack(k + 1)  # k번 요소를 포함하지 않음
# #
# #
# # backtrack(0)
#
#
# # cnt = 0
# # def backtrack(k, cur):  # 현재까지 포함된 요소들의 합
# #     global cnt
# #     if cur > 10:
# #         return
# #     if k == N:
# #         if cur == 10:
# #             cnt += 1
# #     else:
# #         # A.append(arr[k])
# #         backtrack(k + 1, cur + arr[k])  # k번 요소를 포함
# #         # A.pop()
# #         backtrack(k + 1, cur)  # k번 요소를 포함하지 않음
# # backtrack(0, 0)
# # print(cnt)

