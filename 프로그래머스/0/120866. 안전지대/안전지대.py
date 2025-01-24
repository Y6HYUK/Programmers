def solution(board):
    # 전체 칸 : n x n 배열을 리스트 형식으로 나타냄
    # 지뢰가 있는 곳을 ( , ) 형식으로 표현하기
    # 그러면 해당 위치로부터 -1, +1 위치의 부분을 1로 나타내고 0의 값만 추출하면 됨
    
    bomb_list = []
    for idx_row, ele in enumerate(board):
        num_row = idx_row + 1 # 각 행의 번호를 알아내기 위함
        # print(ele)
        
        # 폭탄이 있으면 해당 지역의 주변을 다 1로 만들어야함
        for idx_bomb, bomb in enumerate(ele): # 폭탄의 위치를 알아내기 위한 메서드
            if bomb == 1:
                bomb_list.append((num_row, idx_bomb + 1)) # 리스트에 폭탄의 위치가 저장됨
    
    # print(bomb_list)
    
    # 위험지역 설정
    danger_area = [(-1,-1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)] 
    for i, j in bomb_list:
        for r, c in danger_area:
            da_r = (i-1) + r
            da_c = (j-1) + c
            
            if 0 <= da_r < len(board) and 0 <= da_c < len(board):
                board[da_r][da_c] = 1
    
    answer = 0
    for ele in board:
        answer += ele.count(0)
        
    # print(answer)
    
    return answer
        
    
        
        
