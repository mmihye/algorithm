def solution(s):
    p=0
    y=0
    
    for i in s:
        if(i=='p' or i=='P'):
            p+=1
        elif(i=='y' or i=='Y'):
            y+=1
            
    return p==y
    
# 집계함수 count() 사용
# 문자열 안에서 찾고 싶은 문자의 개수를 찾을 수 있다.
# return s.lower().count('p') == s.lower().count('y')