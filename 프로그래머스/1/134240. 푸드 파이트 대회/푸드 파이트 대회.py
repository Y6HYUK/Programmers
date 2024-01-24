def solution(food):
    
    A = []
    B = []
    for i in range(1,len(food)):
        
        A.append(food[i]//2)
        
    for j in range(1,len(A)+1):
        
        if A[j-1] * str(j) != '':
            B.append(A[j-1] * str(j))
    
    B_str = ''.join(B)
    B_reverse = B_str[::-1]    
            
    answer = B_str + '0' + B_reverse
    
    
    #print(A)
    #print(B)    
    #print(B_str)
    #print(B_reverse)
    print(answer)
    return answer