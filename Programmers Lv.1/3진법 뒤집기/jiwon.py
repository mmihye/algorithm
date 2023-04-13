def solution(n):
    answer=0
    answer_str = ""
    while n>=3:
        answer_str+=str(n%3)
        n//=3
    answer_str+=str(n)
    answer_str = str(int(answer_str))
    
    for idx, i in enumerate(answer_str[::-1]):
        answer += int(i)*(3**idx)
    
    return answer

# int(문자열, 3) -> 문자열을 3진법으로 바꿔줌
# 몫이 0일때까지 무한루프 돌리고 나머지만 넣어주면 됨
# 거꾸로 출력
# range(n, 0, -1) 또는 reversed(range(n))