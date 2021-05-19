#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <string>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    
    deque<int> dualPriorityQueue;
    
    for(string operation : operations){
        if(operation[0] == 'I'){
            dualPriorityQueue.push_back(stoi(operation.substr(2, operation.length()-2)));
            sort(dualPriorityQueue.begin(), dualPriorityQueue.end(), less<int>());
        }
        else if(operation == "D 1"){
            if(dualPriorityQueue.empty()) continue;
            dualPriorityQueue.pop_back();
        }
        else{
            if(dualPriorityQueue.empty()) continue;
            dualPriorityQueue.pop_front();
        }
    }
    
    if(dualPriorityQueue.empty()) return {0, 0};
    else return {dualPriorityQueue[dualPriorityQueue.size()-1], dualPriorityQueue[0]};
}
