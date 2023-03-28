def solution(food):
    answer = ''

    for i in range(len(food)):
        n = food[i] // 2
        for _ in range(n):
            answer += str(i)

    answer2 = answer[::-1]
    answer += '0'
    answer += answer2

    return answer