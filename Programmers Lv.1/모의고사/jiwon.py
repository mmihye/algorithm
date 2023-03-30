def solution(answers):
    students = [
        [1,2,3,4,5], 
        [2,1,2,3,2,4,2,5], 
        [3,3,1,1,2,2,4,4,5,5]]
    students_answer=[0 for i in range(3)]
    answer = []
    
    for i in range(len(answers)):
        for j in range(len(students)):
            if k >= i:
                k=i%len(students[j])
            if answers[i] == students[j][k]:
                students_answer[j]+=1
    
    answer_max = max(students_answer)
            
    return [i+1 for i in range(len(students_answer)) if students_answer[i]==answer_max]