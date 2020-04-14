from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)

    queue = deque([(begin, 0)])

    return BFS(queue, target, words, visited)  
    
def BFS(queue, target, words, visited):
    while True:
        if not(queue):
            return 0
        
        popFromQueue = queue.popleft()

        if popFromQueue[0] == target:
            return popFromQueue[1]
        else:
            for i in range(len(words)):
                if not(visited[i]) and isDifferOne(popFromQueue[0], words[i]):
                    visited[i] = True
                    queue.append((words[i], popFromQueue[1]+1))

def isDifferOne(word1, word2):
    count = 0
    
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    
    return (count == 1)
