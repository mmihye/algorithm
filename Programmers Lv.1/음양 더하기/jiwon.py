def solution(absolutes, signs):
    return sum([absolutes[idx] if(i) else -absolutes[idx] for idx,i in enumerate
                (signs)])

# zip() - 여러 개의 순회 가능한 객체를 인자로 받아, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자를 반환
# numbers = [1,2,3]
# letters = ["A","B","C"]
# for pair in zip(numbers, letters)
# print(pair)
# (1, 'A')
# (2, 'B')
# (3, 'C)
# return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))