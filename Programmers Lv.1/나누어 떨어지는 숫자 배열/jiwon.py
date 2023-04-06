def solution(arr, divisor):
    answer = []
    
    if(divisor==1):
        return sorted(arr)
    for i in arr:
        if(i%divisor == 0):
            answer.append(i)
    return sorted(answer) if(len(answer)>0) else [-1]

# for문 if문 한줄로
# i for i in arr if(i%divisor==0)
# 파이썬 or
# return sorted([n for n in arr if n%divisor == 0]) or [-1]
# 앞에 것이 거짓일 때 뒤에 것 호출. 빈 리스트는 False