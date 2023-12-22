def solution(numbers):
    
    A = [0,1,2,3,4,5,6,7,8,9]
    numbers.sort()
    
    for i in numbers:
        for j in A:
            if i == j:
                A.remove(j)
                
    answer = sum(A)
    return answer