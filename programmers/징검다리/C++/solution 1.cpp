#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int first = 0, last = distance, mid, delete_count, answer;
	
	rocks.push_back(first);
	rocks.push_back(last);
	
	sort(rocks.begin(), rocks.end());
	
	bool isExactCaseAvailable = false;
	
	while(first <= last){
		mid = (first + last) / 2;
		delete_count = 0;
		int i = 0;
		
		while(i<rocks.size()-1){
			// mid 값에 비해 dist가 작은 경우, 다른 바위를 제거하였을 때도 그러한지 체크한다.
			if((rocks[i+1] - rocks[i]) < mid){
				bool isValid = false;
				
				// j가 1부터 시작하는 이유는 (i+2)번째 바위부터 마지막 바위까지 제거하면서 체크해볼 것이기 때문.
				for(int j=1; j<rocks.size()-i-1; j++){
					int dist = rocks[i+1+j] - rocks[i];
					
					// 그러다가 mid보다 크거나 같은 경우가 생기면, ok!
					// 그 위치로 jump한다(i += j+1)
					if(dist >= mid){
						isValid = true;
						delete_count += j;
						i += j+1;
						break;
					}
				}
				
				// 가능한 경우를 탐색했는데도 전부 mid보다 작은 경우
				if(!isValid){
					// 첫번째 dist인데도 만족하지 않는다면, 모든 바위를 다 지워도 안 된다는 것이므로, n보다 큰 숫자를 delete_count에 넣는다. 
					if(i == 0) delete_count = n+1;
					// 중간 dist가 만족하지 않는다면, 그냥 직전의 바위 하나 제거해서, 앞과 같은 valid한 그룹으로 만들면 된다.
					else delete_count += 1;
					
					break;
				}
			}
			// dist값이 mid보다 크거나 같은 제대로 된 경우는 그냥 진행(i += 1)
			else i += 1;
		}
		
		if(delete_count < n){
			first = mid + 1;
			// 정확히 delete_count == n이 되는 경우가 있으면 그게 답! (delete_count가 클수록, 가장 작은 값이 커지기 때문.)
	
			// 그러나 없으면, delete_count < n이 되는 경우의 mid값이, answer의 후보군이 되므로, 저장해둔다!
			// 그 이유는 아무거나 n 값에 맞게 지워버리면 해당 mid 값이 최소값이 되기 때문.
			if(!isExactCaseAvailable) answer = mid;
		}
		else if(delete_count == n){
			first = mid + 1;
			
			// 정확히 delete_count == n이 되는 경우이므로 answer 값을 바꾸고, 이것을 나타내는 boolean var도 값을 바꾼다!
			isExactCaseAvailable = true;
			answer = mid;
		}
		// mid가 너무 크다는 뜻이므로, last 값을 조정한다!
		else last = mid - 1;
	}
	
    return answer;
}
