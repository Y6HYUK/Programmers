def solution(name, yearning, photo):
    # photo의 길이 부터 반복문을 시작해야함.
    # 그래야 photo의 인덱스 1개에 name 개수만큼 반복됨
    
    B = []
    for i in range(len(photo)):
        A = []
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if name[k] == photo[i][j]:
                    A.append(yearning[k])
        B.append(sum(A))
    #print(A)
    #print(B)
    
    
    
    answer = B
    return answer