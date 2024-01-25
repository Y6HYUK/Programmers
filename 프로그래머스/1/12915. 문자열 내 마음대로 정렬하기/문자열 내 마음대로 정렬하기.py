def solution(strings, n):
    strings.sort()
    New_strings = sorted(strings, key = lambda x : x[n])
    #print(strings)
    #print(New_strings)
    answer = New_strings
    return answer