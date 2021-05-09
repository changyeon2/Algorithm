#include <string>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;
	
	sort(routes.begin(), routes.end(), [](auto vec1, auto vec2){
		return (vec1[0] > vec2[0]);
	});
		
	stack<vector<int>> s;
	
	for(vector<int> route : routes) s.push(route);
	
	vector<int> popedVector;
	vector<int> topOfStack;
	
	while(true){
		if(s.size() == 1){
			answer++;
			s.pop();
			break;
		}
		
		popedVector = s.top();
		s.pop();
		topOfStack = s.top();
		
		if(popedVector[1] >= topOfStack[0] && popedVector[1] <= topOfStack[1]){
			topOfStack[1] = popedVector[1];
			s.pop();
			s.push(topOfStack);
		}
        
		else if(topOfStack[1] < popedVector[1]) continue;
		
        	else answer++;
	}
	
    return answer;
}
