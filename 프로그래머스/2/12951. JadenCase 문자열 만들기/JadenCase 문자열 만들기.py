def solution(s):
    # ' ' (공백)으로 분리하면, 연속된 공백도 빈 문자열로 남게 됩니다.
    s_list = s.split(' ')
    answer = []
    
    for word in s_list:
        # 만약 단어가 빈 문자열이면 그대로 추가
        if word == '':
            answer.append('')
        else:
            word = word.lower()
            # 단어의 첫 글자가 알파벳이면 대문자로 변환
            if word[0].isalpha():
                answer.append(word[0].upper() + word[1:])
            else:
                answer.append(word)
    
    # join 시 ' '을 사용하면, 원래의 공백 개수를 보존할 수 있습니다.
    return ' '.join(answer)
