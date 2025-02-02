def solution(s):
    answer = []
    # 남은 문자열 s가 존재하는 동안 반복
    while len(s) > 0:
        x = s[0]
        count_x = 0
        count_y = 0
        found = False  # 분리 조건이 만족되었는지 플래그로 관리
        
        # s의 각 문자를 인덱스와 함께 순회
        for idx, ch in enumerate(s):
            if ch == x:
                count_x += 1
            else:
                count_y += 1
            
            if count_x == count_y:
                # 조건 만족 시, s의 처음부터 (idx+1)까지가 하나의 부분 문자열
                answer.append(s[:idx+1])
                # s를 남은 부분으로 갱신
                s = s[idx+1:]
                found = True
                break
        
        # for 루프를 끝까지 돌았는데 조건을 만족하지 못한 경우
        if not found:
            answer.append(s)
            break
    
    # 최종적으로 answer에 저장된 부분 문자열 개수를 반환
    return len(answer)
