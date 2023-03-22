def solution(n):
    return int(''.join(sorted(str(n))[::-1]))

# 정수를 문자열로 바꾼다음 sorted()를 통해 정렬해주었다.
# 문자열 정렬:sorted(s) 원본 안바뀜/ 문자열, 리스트 정렬:s.sort() 원본 바뀜
# [::-1]을 통해 뒤집어주고 
# ''.join()으로 리스트를 문자열로 만들어준 다음 
# int()로 정수로 변환해주었다.