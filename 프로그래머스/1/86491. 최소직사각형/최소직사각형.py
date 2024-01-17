def solution(sizes):
    # 세로 길이가 가로 길이보다 길다면 해당 리스트를 뒤집어줌
    
    A = []
    B = []
    
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i].reverse()
        A.append(sizes[i][0])
        B.append(sizes[i][1])
        
    answer = max(A) * max(B)
    
    return answer