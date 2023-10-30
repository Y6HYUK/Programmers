def solution(s):
    L = s.lower() # 문자열 s를 소문자로 변환
    Arr = list(L) # 문자열 A를 리스트로 변환
    if Arr.count('p') == Arr.count('y'):
        answer = True
    elif Arr.count('p') != Arr.count('y'):
        answer = False
    else:
        answer = True

    return answer