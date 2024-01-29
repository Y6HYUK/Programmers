def solution(k, score):
    A = []
    result = []
    
    for i in range(len(score)):
        if i+1 <= k:
            A.append(score[i])
            result.append(min(A))
        else:
            A.sort()
            if A[0] <= score[i]:
                A[0] = score[i]
                result.append(min(A))
            else:
                result.append(A[0])
        
    print(A)
    print(result)
    answer = result
    return answer