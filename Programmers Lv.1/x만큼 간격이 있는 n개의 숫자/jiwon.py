def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer

# 리스트 내 반복문
# return [x*(i+1) for i in range(n)]