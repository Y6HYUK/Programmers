def solution(dartResult):
    # S / D / T : 제곱
    # * 는 2배 / # 는 마이너스
    score = ''
    score_list = []
    for i in dartResult:
        if i.isdigit():
            score += i
            
        elif i == 'S':
            score = int(score) ** 1
            score_list.append(score)
            score = ''
            
        elif i == 'D':
            score = int(score) ** 2
            score_list.append(score)
            score = ''
            
        elif i == 'T':
            score = int(score) ** 3
            score_list.append(score)
            score = ''
            
        elif i == '#':
            score_list[-1] = score_list[-1] * (-1)
        
        elif i == '*':
            if len(score_list) > 1:
                score_list[-1] = score_list[-1] * 2
                score_list[-2] = score_list[-2] * 2
            else:
                score_list[-1] = score_list[-1] * 2
        
    return sum(score_list)