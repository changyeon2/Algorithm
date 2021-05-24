#include <string>
#include <vector>
#include <queue>
#include <deque>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    deque<pair<int, int>> bridge;
    queue<int> trucks;
    
    int answer = 0, currentWeights = 0;
    
    for(int truck: truck_weights){
        trucks.push(truck);
    }
    
    while(true){
        if(!bridge.empty() && bridge.front().second == bridge_length){
            currentWeights -= bridge.front().first;
            bridge.pop_front();
        }
        
        if(!trucks.empty() && currentWeights + trucks.front() <= weight){
            bridge.push_back({trucks.front(), 0});
            currentWeights += trucks.front();
            trucks.pop();
        }
        
        for(deque<pair<int, int>>::iterator iter=bridge.begin(); iter!=bridge.end(); iter++){
            iter->second++;
        }
        
        answer++;
        
        // 여기까지 왔다는 건, 한번 진행했다는 뜻(= 1초가 지났다)
        if(bridge.empty()) return answer;
    }
      
    return answer;
}
