def solution(array, commands):
    answer = []
    for i,command in enumerate(commands):
        arr = array[command[0]-1:command[1]]
        arr.sort()
        #answer[i] = arr[command[2]-1]
        answer.append(arr[command[2]-1])
        print(arr)
        print(i)
    return answer