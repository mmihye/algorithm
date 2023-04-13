def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for idx, i in enumerate(lost):
        if i in reserve:
            lost[idx]=-1
            reserve.remove(i)
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len([i for i in lost if i!=-1])