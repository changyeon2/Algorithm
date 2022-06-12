from collections import defaultdict
import math

maxtime = 23*60 + 59

def solution(fees, records):
    database = defaultdict(int)
    times = defaultdict(int)
    results = defaultdict(int)
    
    for record in records:
        record = record.split(" ")
        # 0: 시각, 1: 차량번호, 2: 내역
        
        if record[2] == "OUT":
            timediff = ((int(record[0][0])*10 + int(record[0][1])) * 60 + int(record[0][3])*10 + int(record[0][4])) - database[record[1]]
            
            times[record[1]] += timediff
            
            del database[record[1]]
        else:
            database[record[1]] = (int(record[0][0])*10 + int(record[0][1])) * 60 + int(record[0][3])*10 + int(record[0][4])
        
    for remain in list(database.keys()):
        timediff = maxtime - database[remain]

        times[remain] += timediff
    
    for car, time in list(times.items()):
        time -= fees[0]
        
        if time <= 0: results[car] += fees[1]
        else: results[car] += fees[1] + math.ceil(time / fees[2]) * fees[3]
    
    answer = [x[1] for x in sorted(results.items(), key=lambda x: int(x[0]))]

    return answer
