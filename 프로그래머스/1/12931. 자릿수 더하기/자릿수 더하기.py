def solution(n):
    A = list(str(n))
    answer = 0
    for i in A:
        answer += int(i)
    
    return answer