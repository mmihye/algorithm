def solution(seoul):
    idx = 0
    for i in seoul:
        if i=="Kim":
            break
        idx += 1
    return "김서방은 "+str(idx)+"에 있다"

# 리스트 인덱스 반환
# seoul.index("Kim")