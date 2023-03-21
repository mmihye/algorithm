def solution(n):
    min = 0
    for i in range(2,n):
        if n%i == 1:
            min = i
            break
    return i