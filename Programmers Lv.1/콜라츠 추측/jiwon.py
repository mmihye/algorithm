def solution(num):
    n=num
    i=0
    while n!=1 and i<=500:
        if n%2==0:
            n //= 2
            i += 1
        else:
            n = n*3+1
            i += 1
        if n==num:
            return -1
    return i if(i<=500) else -1