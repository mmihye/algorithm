def solution(s):
    answer=""
    isOdd = True
    print(s.split(" "))
    
    for idx,i in enumerate(s):
        if i==" ":
            answer += " "
            isOdd = True
            continue
            
        if isOdd:
            answer += s[idx].upper()
            isOdd = False
        else:
            answer += s[idx].lower()
            isOdd = True
            
    return answer

# s.split(" ")를 써서 단어마다 끊을 수 있다. -> 문자열 리스트로 반환함.
# ['try', 'hello', 'world]
# for i in s.split(" ")
# 람다
# return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))