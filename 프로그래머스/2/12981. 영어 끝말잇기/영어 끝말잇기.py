def solution(n, words):
    answer = [words[0]]
    # 맨 마지막, 스펠링과 맨 앞의 스펠링이 같은지 확인해야함
    # 단어의 길이가 길지 않으므로, 하나씩 추가하면서 비교하기
    for i in range(1, len(words)):
        if words[i] not in answer and answer[i-1][-1] == words[i][0]:
            answer.append(words[i])
            
        else:
            if (i+1) % n == 0:
                person = n
                num = (i+1) // n
            else:
                person = (i+1) % n
                num = ((i+1) // n) + 1
            
            return [person, num]
            
    return [0,0]

