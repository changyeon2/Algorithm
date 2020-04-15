# main idea : Backtracking Algorithm

from collections import deque

answer = []

def solution(tickets):
    airportDict = dict()
    visited = dict()
    stack = deque([('ICN', 0)])
    
    for i in range(len(tickets)):
        if airportDict.get(tickets[i][0]) == None:
            airportDict[tickets[i][0]] = [tickets[i][1]]
        else:
            airportDict[tickets[i][0]].append(tickets[i][1])
        
        if visited.get((tickets[i][0], tickets[i][1])) != None:
             visited[(tickets[i][0], tickets[i][1])] += 1
        else:
             visited[(tickets[i][0], tickets[i][1])] = 1
    
    for x in list(airportDict.keys()):
        airportDict[x].sort()
    
    DFS(airportDict, stack, len(tickets), visited)

    return answer

def DFS(airportDict, stack, numOfTicket, visited):
    global answer

    topOfStack = stack.pop()

    answer.append(topOfStack[0])

    if topOfStack[1] == numOfTicket:
        return True
    
    if airportDict.get(topOfStack[0]) == None or not(airportDict[topOfStack[0]]):
        answer.pop()
        return False

    for i in range(len(airportDict[topOfStack[0]])):
        if visited[(topOfStack[0], airportDict[topOfStack[0]][i])] != 0:
            visited[(topOfStack[0], airportDict[topOfStack[0]][i])] -= 1
            
            stack.append((airportDict[topOfStack[0]][i], topOfStack[1]+1))

            result = DFS(airportDict, stack, numOfTicket, visited)

            if result:
                return True
            else:
                visited[(topOfStack[0], airportDict[topOfStack[0]][i])] += 1
    
    answer.pop()
    return False
    
