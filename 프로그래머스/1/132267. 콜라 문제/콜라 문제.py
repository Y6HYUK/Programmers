def solution(a, b, n):
    
    A = []
    while n >= a:
        spare = n % a # 나머지
        receive = (n//a) * b # 몫
        A.append(receive)
        n = spare + receive
        
    answer = sum(A)
    
    return answer