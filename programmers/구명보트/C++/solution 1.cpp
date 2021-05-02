// C++ vector erase ->  O(N2) time complexity
// So, instead of deleting elements of vector, I used an indexing method(head, tail).

#include <vector>
#include <algorithm> // for sort function
#include <functional> // for greater function
#include <cmath> // for ceil function

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
	
	int head = 0, tail = people.size()-1;	
	
	sort(people.begin(), people.end(), greater<int>());
	
	while(head <= tail){
		if(people[head] <= (limit / 2)){
			answer += ceil((float)(tail - head + 1) / 2);
			break;
		}
		
		if(people[head] + people[tail] <= limit){
			tail--;
		}
		
		head++;
		
		answer++;
	}
	
    return answer;
}
