def solution(n):
    # 5 => 1, (2, 4), 5
    # 6 => 1, (2), 3, (6)
    
    # 5000 => 2500 -> 1250 -> 625 ( 624 + 1),
    # 624 -> 312 -> 156 -> 78 -> 39 (38 + 1),
    # 38 -> 19 (18 + 1),
    # 18 -> 9 (8 + 1),
    # 8 -> 4 -> 2 -> (1)
    
    count = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
            
        else:
            n -= 1
            count += 1
            
    print(count)
    return count
            
    
    