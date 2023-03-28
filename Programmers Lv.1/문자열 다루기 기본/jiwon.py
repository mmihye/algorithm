def solution(s):
    if len(s)!=4 and len(s)!=6:
        return False
    for i in s:
        if(i<"0" or i>"9"):
            return False
    return True

# 숫자로만(음수, 실수 x) 이루어져있는지 체크하는 함수 - isdigit()
# 알파벳으로만 이루어져 있는지 체크하는 함수 - isalpha()
# 해당 구간에 있는지 확인 - len(s) in [4,6]
# return s.isdigit() and len(s) in [4,6]