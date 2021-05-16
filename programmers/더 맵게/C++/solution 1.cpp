#include <string>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

int solution(vector<int> scoville, int K) {
	int answer = 0;
	
	priority_queue<int, vector<int>, greater<int>> pq;
	
	for(int pungency : scoville) pq.push(pungency);
	
	int firstNonPungentFood;
	int secondNonPungentFood;
	
	while(true){
		if(pq.top() >= K) return answer;
		
		if(pq.size() == 1 && pq.top() < K) return -1;
		
		firstNonPungentFood = pq.top(); pq.pop();
		
		secondNonPungentFood = pq.top(); pq.pop();
		
		pq.push(firstNonPungentFood + secondNonPungentFood * 2);
		
		answer++;
	}
}
