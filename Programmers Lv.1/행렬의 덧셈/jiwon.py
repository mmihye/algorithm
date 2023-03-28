def solution(arr1, arr2):
    answer = []
    for i, n1 in enumerate(arr1):
        temp = []
        for j, n2 in enumerate(arr1[i]):
            temp.append(n2+arr2[i][j])
        answer.append(temp)
    return answer

# for x in zip(arr1, arr2)] 후
# list(map(sum, zip(*x))) 하면
# 왜 섞이는건지 이해가 안감