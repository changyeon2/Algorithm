#include <string>
#include <vector>
#include <queue>

using namespace std;

auto compareByfirst = [](const vector<int>& vec1, const vector<int>& vec2){
  // 시작시간이 같으면, 더 짧게 걸리는 작업이 먼저 heap에서 나올 수 있도록 해야 함!
	if(vec1[0] == vec2[0]) return (vec1[1] > vec2[1]);
	else return (vec1[0] > vec2[0]);
};

auto compareBySecond = [](const vector<int>& vec1, const vector<int>& vec2){
	return (vec1[1] > vec2[1]);
};

int solution(vector<vector<int>> jobs) {
	int answer = 0, currentTime = 0;

	priority_queue<vector<int>, vector<vector<int>>, decltype(compareByfirst)> minHeapByFirst(compareByfirst);
	
	for(vector<int> job : jobs) minHeapByFirst.push(job);
	
	while(!minHeapByFirst.empty()){
		if(minHeapByFirst.top()[0] > currentTime){
			answer += minHeapByFirst.top()[1];
			currentTime = minHeapByFirst.top()[0] + minHeapByFirst.top()[1];
			minHeapByFirst.pop();
		}
		else{
			priority_queue<vector<int>, vector<vector<int>>, decltype(compareBySecond)> minHeapBySecond(compareBySecond);
			
			while(!minHeapByFirst.empty() && minHeapByFirst.top()[0] <= currentTime){
				minHeapBySecond.push(minHeapByFirst.top()); minHeapByFirst.pop();
			}
			
			answer += (currentTime - minHeapBySecond.top()[0]) + minHeapBySecond.top()[1];
			currentTime += minHeapBySecond.top()[1];
			minHeapBySecond.pop();
			
			while(!minHeapBySecond.empty()){
				minHeapByFirst.push(minHeapBySecond.top()); minHeapBySecond.pop();
			}
		}
	}
	
	return answer / jobs.size();
}
