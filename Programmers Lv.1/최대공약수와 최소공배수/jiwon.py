def solution(n, m):
    if n>m:
        n,m = m,n
    elif n==m:
        return [n,n]
    
    r1=1
    r2=1
    
    # n의 약수
    n_arr = [i for i in range(1,n+1) if(n%i==0)]
    # 최대공약수
    for i in n_arr[::-1]:
        if m%i==0:
            r1=i
            break
    
    # 최소공배수
    n1 = n
    m1 = m
    for i in n_arr[::-1]:
        if n1%i==0 and m1%i==0:
            r2 *= i
            n1//=i
            m1//=i
    r2 *= n1*m1
    return [r1, r2]

# a,b가 있을 때 최대 공약수 공식(유클리드 호제법)
# c,d = max(a, b), min(a, b)
# t = 1
# while t>0:
#   t = c%d
#   c, d = d, t
#   answer = [ c, int (a*b/c)]
# 최소공배수 = a*b/(최대공약수)
# 또는 최대공약수 import math 후 math.gcd(a,b)
# 최소공배수 math.lcm(a,b)