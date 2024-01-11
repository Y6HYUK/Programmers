def solution(t, p):
    
    num = len(list(p)) # p의 길이
    
    A = []
    for i in t:
        A.append(i)
    print(A)
    
    C = []
    for j in range(len(A)):
         C.append(A[j:j+num])
    
    if len(C) > len(list(t)) - num + 1:
        rule = len(C) - (len(list(t))- num + 1)
        
        C = C[:-rule]
    #규칙 : C의 길이가 문자열 t개수 - 문자열 p개수 +1 보다 크다면,
    #초과되는 수를 C에서 제외
    
    D = []
    for k in C:
        D.append(''.join(k))
        
    E = []
    for i in D:
        if i <= p:
            E.append(i)
    print(E)

    answer = len(E)
    return answer