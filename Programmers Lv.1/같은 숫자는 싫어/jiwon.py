def solution(arr):
    result_arr = []
    for idx, i in enumerate(arr):
        if idx==0 or result_arr[-1]!=arr[idx]:
            result_arr.append(arr[idx])
    return result_arr

# result_arr[-1:]을 하면 result_arr이 빈 배열일 경우에도 빈 리스트로 반환한다.
# -> idx==0을 해줄 필요가 없어짐