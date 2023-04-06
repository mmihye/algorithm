def solution(x):
    x_sum=0
    for i in str(x):
        x_sum += int(i)
    return x%x_sum==0

# sum() 생각하기^^
# return x%sum(int(i) for i in str(x)) == 0