def solution(s):
    answer = []
    while len(s) > 0: # 문자열 s의 길이가 0이 될때까지
        x = s[0] # 맨 처음 문자열
        count_x = 0
        count_y = 0
        ### 마지막 해결책에서 len(s) == 1 만으로는 조건을 만족시키지 못함 ###
        ### 조건을 확인할 수 있는 변수가 필요함 ###
        disting = False
        
        for i in s:
            if i == x:
                count_x += 1
            else:
                count_y += 1
                
            if count_x == count_y: # 횟수가 같아지면 문자열 분리
                answer.append(s[:count_x+count_y])
                s = s[count_x+count_y:] # 문자열 분리
                disting = True
                break
        
        if disting == False: # 만약 마지막에 문자열이 1개만 남는다면, 처리해주기
            answer.append(s)
            break
            
    return len(answer)