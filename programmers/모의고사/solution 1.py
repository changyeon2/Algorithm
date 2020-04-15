def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == person1[i%5]:
            correct[0] += 1
        if answers[i] == person2[i%8]:
            correct[1] += 1
        if answers[i] == person3[i%10]:
            correct[2] += 1    
    
    maxCorrect = max(correct)
    answer = []
    
    for i in range(3):
        if correct[i] == maxCorrect:
            answer.append(i+1)
        
    return answer
