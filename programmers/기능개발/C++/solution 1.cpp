#include <string>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    stack<pair<int, int>> developStack;
    
    int currentTime;
    
    for(int i=progresses.size()-1; i>=0; i--){
        developStack.push({progresses[i], speeds[i]});
    }
    
    while(!developStack.empty()){
        int publishCount = 0;
        
        currentTime = ceil(((double)(100-developStack.top().first) / developStack.top().second));
        
        developStack.pop();
        publishCount++;
        
        while(!developStack.empty() && ((developStack.top().first) + (developStack.top().second)*currentTime) >= 100){
            developStack.pop();
            publishCount++;
        }
        
        answer.push_back(publishCount);
    }
    
    return answer;
}
