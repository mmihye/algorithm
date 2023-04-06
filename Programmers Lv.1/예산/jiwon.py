def solution(d, budget):
    temp=0
    answer=0
    if sum(d) <= budget:
        return len(d)
    for idx, i in enumerate(sorted(d)):
        temp+=i
        if(temp>budget):
            answer=idx
            break
    return answer

# enumerate와 temp 안쓰고 풀 수 있었다 -.-;