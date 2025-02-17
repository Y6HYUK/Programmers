def solution(A,B):
    
    # 로직 : A의 최대와 B의 최소가 곱해져야함
    A.sort(reverse = True)
    print(A)
    B.sort()
    print(B)
    
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
        
    print(answer)
    
    return answer