def solution(phone_number):
    phone_len = len(phone_number)
    return ''.join(["*" for i in range(0, phone_len-4)]+[phone_number[i] for i in range(phone_len-4,phone_len)])

# 문자열 곱하기
# "*"*5 -> *****
# 인덱스
# [-4:] -> 끝에서 4번째부터 끝까지 출력
# a[start : end : step] -> start부터 step 간격으로 end-1 까지