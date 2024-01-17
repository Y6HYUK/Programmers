def solution(number):
    a = len(number)
    
    count = 0
    for i in range(a):
        for j in range(i+1, a):
            for k in range(j+1, a):
                if number[i] + number[j] + number[k] == 0:
                    count +=1
                  

    answer = count
    return answer