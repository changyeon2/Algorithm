#include <string>
#include <vector>

using namespace std;

long long solution(int n, vector<int> times) {
    // Solution
    // 시간의 최소값은 심사하는 시간이 가장 짧은 한 명이 끝나기까지의 시간(최소 한 명이 한 번은 일해야하니까),
    // 시간의 최대값은 심사하는 시간이 가장 짧은 한 명"만" 일하는 worst case의 시간이다.
    // binary search를 하면서, 다같이 일하는 better case가 있는지 확인하는데, 
    // 총 처리할 수 있는 사람 수가 n이 되는 시간 중에 가장 최소값을 return하면 된다.

    // Find min value among elements of times
    // 이걸 long long으로 안 해주면 n * fastest_person (i.e. int * int 연산)에서
    // 32bit를 초과하는 부분이 날아가게 된다.
    long long fastest_person = 1000000000;

    for(int i=0; i<times.size(); i++){
        if(times[i] < fastest_person){
            fastest_person = times[i];
        }
    }

    // Binary search
    long long start = fastest_person;
    long long end = n * fastest_person;
    long long min_time = n * fastest_person;
    long long checked_person = 0;

    while(start <= end){
        long long mid = (start + end) / 2;
        checked_person = 0;

        for(int i=0; i<times.size(); i++){
            checked_person += mid / times[i];

            // long long인 애들 계속 더하다보면, long long 범위도 초과할 수 있다!
            // 따라서 checked_person > n인 경우는 이 for문 안에서 체크해야한다!
            // (checked_person == n인 경우까지 포함하는 이유는, 여기서 mid_time 값을 바꾸기 때문)
            if(checked_person >= n){
                // 일단 이 경우도 mid_time이 될 수 있으므로, 저장!
                // end를 하나 줄여가면서 더 짧게 걸리는 시간이 있는지 체크한다.
                min_time = mid;
                end = mid - 1;
                break;
            }
        }

        if(checked_person < n) start = mid + 1;     
    }


    return min_time;
}
