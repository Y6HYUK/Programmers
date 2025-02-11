def solution(citations):
    # 논문 n개 / 인용 h편 
    answer = []
    for i in range(max(citations)+1):
        # i번 인용된 논문이 몇 편 이상인지?
        count = 0
        for j in citations:
            if j >= i:
                count += 1
                
        # print(count)
        answer.append(count)
    
    new_answer = []
    for k in range(len(answer)):
        if k <= answer[k]:
            new_answer.append(k)
        
    # print(answer)
    # print(new_answer)
    
    return max(new_answer)