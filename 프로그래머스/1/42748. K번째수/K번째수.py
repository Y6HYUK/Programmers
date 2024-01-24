def solution(array, commands):
    
    #print(commands[0].index(3))
    New_array = []
    # commands의 길이가 주어져야함
    for i in range(len(commands)):
        A = commands[i]
        #print(A)
        New_array.append(array[A[0]-1 : A[1]])
        
        New_array[i].sort()
        
        #print(New_array)
        New_array[i] = New_array[i][A[2]-1]
        
    print(New_array)
        


    answer = New_array
    return answer