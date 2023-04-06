def solution(left, right):
    odd_sum = 0
    even_sum = 0
    for i in range(left, right+1):
        if(i == int(i**0.5)**2):
            odd_sum += i
        else:
            even_sum += i
    return even_sum-odd_sum