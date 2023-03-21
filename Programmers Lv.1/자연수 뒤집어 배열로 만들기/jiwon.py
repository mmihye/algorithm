def solution(n):
    return [int(i) for i in str(n)[::-1]]

# 리스트 뒤집기
# 1. [::-1]
# 2. reversed -> reversed(str(n))