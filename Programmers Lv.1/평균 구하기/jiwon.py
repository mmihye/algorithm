def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum += i
    answer = sum/len(arr)
    return answer

# 파이썬 배열 합  내장함수 sum()이 있는 걸 몰랐다.
# def solution(arr):
#     return sum(arr)/len(arr)