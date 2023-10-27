def solution(n):
    A = []
    for i in range(1,n+1):
        if n%i == 0:
            A.append(i)
    answer = sum(A)
    return answer