def solution(arr1, arr2):
    
    length_list = len(arr1) #리스트의 인덱스 개수
    length_sub_list = len(arr1[0]) #리스트 내의 0번 인덱스의 length

    C = []

    for i in range(length_list):
        B = []
        for j in range(length_sub_list):
            A = (arr1[i][j] + arr2[i][j])
            B.append(A)

        C.append(list(B))

    return C