def solution(arr, divisor):
    A = []
    for i in arr:
        if i % divisor == 0:
            A.append(i)                
    A.sort()
        
    if len(A) == 0:
        A = [-1]
    
    return A