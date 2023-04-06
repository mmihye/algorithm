def solution(number):
    answer = 0
    search = 0
    for idx,i in enumerate(number[:-2]):
        for idx2,j in enumerate(number[idx+1:-1]):
            search=-i-j
            answer+=number[idx+idx2+2:].count(search)
    return answer