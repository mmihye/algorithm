def solution(n):
    return ((n**0.5)+1)**2 if (n%n**0.5==0) else -1

# 제곱: **, pow
# x**y = x^y
# pow(x,y) = x^y