def solution(n, arr1, arr2):
    
    # 주어진 10진법을 2진법으로 수정해야함
    A = []
    for i in range(n):
        
        for k in range(n,0,-1):
            if 2**(k-1) > arr1[i]:
                A.append(0)
            else:
                A.append(1)
                arr1[i] = arr1[i] - 2**(k-1)
        
    B = []
    for i in range(n):
        
        for k in range(n,0,-1):
            if 2**(k-1) > arr2[i]:
                B.append(0)
            else:
                B.append(1)
                arr2[i] = arr2[i] - 2**(k-1)
                
    C = []
    for i in range(len(A)):
        if A[i] == 0 and B[i] == 0:
            C.append(0)
        else:
            C.append(1)
    #print(A)
    #print(B)
    #print(C)            
    
    for i in range(len(C)):
        if C[i] == 1:
            C[i] = '#'
        else:
            C[i] = ' '
            
    #print(C)
    
    D = []
    for i in range(n):
        D.append(C[n*i:n*(i+1)])
    #print(D)
    
    for i in range(len(D)):
        D[i] = ''.join(D[i])
        
    #print(D)
        
        
    #for i in range(n,0,-1):
    #    print(i-1)
    answer = D
    return answer