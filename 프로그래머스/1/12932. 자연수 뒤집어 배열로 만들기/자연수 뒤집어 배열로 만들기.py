def solution(n):
    A = list(str(n))
    A = A[::-1]
    B = []
    for i in A:
        B.append(int(i))
    answer = B
    return answer