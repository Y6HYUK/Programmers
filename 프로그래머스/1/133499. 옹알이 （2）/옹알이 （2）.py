def solution(babbling):
    able = ['aya', 'ye', 'woo', 'ma']
    answer = []
    
    for bab in babbling:
        previous = ''
        while len(bab) != 0:
            for i in able:
                if bab.startswith(i) and i != previous:  # 맨 앞 단어를 처리
                    previous = i
                    bab = bab[len(i):]  # 맨 앞 부분 제거
                    break
            else:
                break  # 더 이상 처리할 단어가 없으면 루프 종료
        
        if len(bab) == 0:  # 문자열이 모두 제거되었다면 발음 가능
            answer.append("")
        else:  # 발음 불가능한 단어
            answer.append(bab)
    
    return answer.count("")
