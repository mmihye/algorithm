def solution(s, n):
    answer=''
    atoz = ord('z')-ord('a')+1
    for i in s:
        if(i.islower()):
            s[i] = (ord(i)+n-ord('a'))%atoz+ord('a')
        elif(i.isupper()):
            s[i] = (ord(i)+n-ord('A'))%atoz+ord('A')
    return s

# islower()와 isupper() 로 알파벳 대소문자 확인 가능