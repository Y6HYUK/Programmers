def solution(wallet, bill):
    width = bill[0] # 지폐의 가로
    height = bill[1] # 지폐의 세로
    
    count = 0
    while True:
        
        if (width <= wallet[0] and height <= wallet[1]) or (width <= wallet[1] and height <= wallet[0]):
            return count
            break
    
        if width >= 1 and width > height:
            width /= 2
            width = int(width)

        elif height >= 1 and width < height:
            height /= 2
            height = int(height)
            
        count += 1
        
        