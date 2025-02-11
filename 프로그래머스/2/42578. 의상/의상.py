def solution(clothes):
    dic_clothes = {}
    
    for i in clothes:
        if i[1] not in dic_clothes:
            dic_clothes[i[1]] = 1
            
        else:
            dic_clothes[i[1]] += 1     
    # 경우의 수 
    # 꼭 입어야 하는 것은 아니기에, (각 카테고리의 value + 1) x len(dic_clothes)
    # 모두 안입은 경우의수 1을 빼줘야함
    answer = 1
    for j in dic_clothes.values():
        answer *= j+1
    return answer - 1
    
    
    
