def solution(d, budget):
    d.sort()
    
    if sum(d) <= budget:
        answer = len(d)
    else:
        A = []
        answer = 0
        for i in d:
            A.append(i)
            if sum(A) <= budget:
                answer += 1
            
                
    return answer