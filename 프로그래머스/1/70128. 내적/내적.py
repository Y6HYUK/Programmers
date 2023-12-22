def solution(a, b):
    C = []
    
    for i in range(len(a)):
        C.append(a[i]*b[i])
        
    answer = sum(C)
    return answer