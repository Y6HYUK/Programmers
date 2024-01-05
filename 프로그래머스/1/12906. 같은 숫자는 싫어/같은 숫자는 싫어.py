def solution(arr):
    A = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            A.append(arr[i])
    if arr[len(arr)-2] != arr[len(arr)-1]:
        A.append(arr[len(arr)-1])
    else:
        A.append(arr[len(arr)-2])
    #print(A)  
    answer = A
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    return answer