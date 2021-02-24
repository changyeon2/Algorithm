#include <string>
#include <vector>

using namespace std;

// 그냥 reserve 입장에서 체육복 없는 lost 애들 최대한 안 겹치게 주면 된다.
// 단지 누구를 줄지 체크하는 것을 lost 기준으로 할 뿐!
// loop를 돌면서, reserve가 lost에게 우선적으로 <-으로 주도록 하고, 그 다음으로 -> 방향을 고려한다.
int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
	
	vector<int> students = vector<int>(n, 0);
	
	for(int lostIndex: lost) students[lostIndex-1] -= 1;
	
	for(int reserveIndex: reserve) students[reserveIndex-1] += 1;
	
	for(int i=0; i<n; i++){
		if(students[i] == -1){
			if(i != (n-1) && students[i+1] == 1){
				students[i] = 0;
				students[i+1] = 0;
			}
			else if(i != 0 && students[i-1] == 1){
				students[i] = 0;
				students[i-1] = 0;
			}
		}
	}
	
	for(int student: students){
		if(student == 0 || student == 1) answer++;
	}
	
    return answer;
}
