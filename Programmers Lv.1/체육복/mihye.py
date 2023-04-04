def solution(n, lost, reserve):
    lost.sort()

    list = []

    for x in reserve:
        if x in lost:
            list.append(x)

    for x in list:
        lost.remove(x)
        reserve.remove(x)

    answer = n - len(lost)

    for x in lost:
        if x - 1 in reserve:
            answer += 1
            reserve.remove(x - 1)
        elif x + 1 in reserve:
            answer += 1
            reserve.remove(x + 1)

    return answer