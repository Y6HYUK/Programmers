from itertools import permutations

def solution(k, dungeons):
    answer = []
    # 테스트 케이스가 적기때문에 모든 경우의 수를 만들어 놓고, 그 안에서 조건을 생성하여
    # 모든 경우에 대한 답을 구하고, 그 중 최대 던전 수를 구하는 로직으로 구성함
    for i in permutations(dungeons, len(dungeons)):
        necessity = k # 현재 피로도
        count = 0 # 완료한 던전 수
        
        # print(i)
        
        for j in i:
            if necessity >= j[0]: # 만약 피로도가 최소 필요도 보다 높다면
                necessity -= j[1] # 현재 피로도에서 소모 피로도를 빼준다
                count += 1 # 던전을 1번 완료하였으므로 1을 더해준다.
                
            else:
                break # 그렇지 않으면 break
        
        answer.append(count) # 탐험할 수 있는 던전 수를 저장하기
    
    # print(answer)
    
    return max(answer)