def solution(n):
    answer = 0
    while n//10 >= 1:
        answer += n%10
        n//=10
    return answer+n

# 재귀함수 활용
# return n%10 + solution(n//10)

# 문자열 리스트 정수 리스트로 변환
# return sum([int(i) for i in str(n)])