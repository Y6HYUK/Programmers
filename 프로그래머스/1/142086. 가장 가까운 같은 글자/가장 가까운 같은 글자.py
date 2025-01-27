def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        
        dic[s[i]] = i
        
    return answer