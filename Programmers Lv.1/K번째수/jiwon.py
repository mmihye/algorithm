def solution(array, commands):
    answer = []
    for i in commands:
        temp = sorted(array[i[0]-1:i[1]])
        answer.append(temp[i[2]-1])
    return answer

# return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]
# map, lambda 사용
# return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))