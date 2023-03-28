def solution(n, arr1, arr2):
    answer = []
    for idx,i in enumerate(arr1):
        temp=''
        while i>0:
            temp+=str(i%2)
            i//=2
        if(len(temp)<n):
            temp+="0"*(n-len(temp))
        arr1[idx]=temp

    for idx, i in enumerate(arr2):
        temp=''
        while i>0:
            temp+=str(i%2)
            i//=2
        if(len(temp)<n):
            temp+="0"*(n-len(temp))
        arr2[idx]=temp
        temp=""
        for i in range(n):
            if(arr2[idx][i]=="0" and arr1[idx][i]=="0"):
                temp+=" "
            else:
                temp+="#"
        arr2[idx]=temp[::-1]
    return arr2

# 오른쪽 정렬 - rjust(전체 자리 숫자, 공백이 있을경우 공백을 채울 텍스트)
# 왼쪽 정렬 - ljust
# bin(number) - 전달받은 integer 과 long integer 자료형을 이진수 문자열로 돌려준다.
# bin(10) -> '0b1010'
# 비트 논리 연산자
# bin(0b1101|0b1001) -> 0b1101