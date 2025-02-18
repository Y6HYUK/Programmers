def solution(n):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
    answer = [0,1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer[n] % 1234567
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n == 1 or n == 2:
#             return 1
#         else:
#             return fibonacci(n-2) + fibonacci(n-1)
        
#     return fibonacci(n) % 1234567