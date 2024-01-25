def solution(numbers):
    
    #numbers = [0,0,10,2,3,9,1,3,2,3,4]
    
    A = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            A.append(numbers[i]+numbers[j])
    print(A)
    
    A = list(set(A))
    A.sort()
    
    answer = A
    return answer