def solution(lottos, win_nums):
    
    # 일단 정렬을 해주는게 좋아보임
    lottos.sort()
    win_nums.sort()
    corrected_list = []
    
    for i in lottos:
        if i in win_nums or i == 0: 
            corrected_list.append(i) # 맞춘 숫자와 절대 숫자0을 리스트로 생성
            
    print(lottos)
    print(win_nums)
    print(corrected_list)
    
    # corrected_list에 절대숫자 0이 몇개인지 확인해야함
    zero_count = corrected_list.count(0)
    # 당첨 번호 개수의 최소, 최대 개수
    corrected_min_max_count = (len(corrected_list) - zero_count, len(corrected_list))
    print(corrected_min_max_count)
    
    # 맞춘 개수 : '순위'
    rank = {6:'1', 5:'2', 4:'3', 3:'4', 2:'5', 1:'6', 0: '6'}
    return [int(rank[corrected_min_max_count[1]]), int(rank[corrected_min_max_count[0]])]
    
    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
            
    # 예시 3, 7, 0, 0, 0, 1
    # 3, 5, 9, 14, 43, 45
    # if len(win_nums) == 0: # 만약 모든 lottos 번호가 일치한다면 1등 당첨
    #     return [1, 1]
    # else:
    #     zero_count = lottos.count(0) # 조작할 수 있는 수의 개수
    #     if zero_count == 6: # 모든 lottos 번호를 조작 가능하다면 1등 혹은 낙첨 가능
    #         return [1, 6]
    #     elif zero_count == 5:
    #         return [2, 5]
            
    