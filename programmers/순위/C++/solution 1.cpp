#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;

    // make 2D matrix
    // -1 -> point간에 연결이 안 되었다는 표시
    vector<vector<int>> graph(n, vector<int>(n, -1));

    for(vector<int> result: results){
        // 1 -> 해당 point가 child인 경우
        // 2 -> 해당 point가 parent인 경우
        graph[result[0]-1][result[1]-1] = 1;
        graph[result[1]-1][result[0]-1] = 2;
    }

    // Floyd-Warshall Algorithm
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            for(int k=0; k<n; k++){
                // point들이 연결이 안 되어있으나, 다른 point를 통해 경로를 만들 수 있으면
                // child(1), parent(2) 표시를 해준다!
                
                // 이 point에서 나가는 방향 체크
                if((graph[i][k] == 1) && (graph[k][j] == 1)){
                    graph[i][j] = 1;
                    graph[j][i] = 2;
                }
                
                // 이 point로 들어오는 방향 체크해줘야 함! (뒤늦게 이어질 수도 있으므로)
                if((graph[i][k] == 2) && (graph[k][j] == 2)){
                    graph[i][j] = 2;
                    graph[j][i] = 1;
                }
            }
        }
    }

    for(vector<int> point: graph){
        // 1과 2 counting (승패가 결정난 경우이므로)
        if((count(point.begin(), point.end(), 1) + count(point.begin(), point.end(), 2)) == n-1){
            answer++;
        }
    }

    return answer;
}
