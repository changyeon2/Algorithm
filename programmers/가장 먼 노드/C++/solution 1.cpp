#include <string>
#include <vector>
// queue는 내부적으로 deque 사용! 고로, 무엇을 include해서 queue를 구현하든 상관없음!
#include <deque>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;

    int* vertex_value = new int[n]; 
    vector<int>* vertices = new vector<int>[n]; 
    deque<int> queue = deque<int>();
    bool* isVisited = new bool[n];

    for(int i=0; i<n; i++){
        vertices[i] = vector<int>();
        vertex_value[i] = -1;
        isVisited[i] = false;
    }

    for(int i=0; i<edge.size(); i++){
        if(edge.at(i).at(0) == 1){
            queue.push_back(edge.at(i).at(1)-1);
            vertex_value[edge.at(i).at(1)-1] = 1;
            continue;
        }

        if(edge.at(i).at(1) == 1){
            queue.push_back(edge.at(i).at(0)-1);
            vertex_value[edge.at(i).at(0)-1] = 1;
            continue;
        }

        vertices[edge.at(i).at(0)-1].push_back(edge.at(i).at(1)-1);
        vertices[edge.at(i).at(1)-1].push_back(edge.at(i).at(0)-1);
    }

    while(queue.size() != 0){
        // pop_front는 아무것도 return 안 함!
        int target_vertex = queue.front();
        queue.pop_front();

        for(int i=0; i<vertices[target_vertex].size(); i++){
            if(vertex_value[vertices[target_vertex][i]] == -1){
                vertex_value[vertices[target_vertex][i]] = vertex_value[target_vertex] + 1;
            }
            else if(vertex_value[vertices[target_vertex][i]] > vertex_value[target_vertex] + 1){
                    vertex_value[vertices[target_vertex][i]] = vertex_value[target_vertex] + 1;
                }
            else{
                continue;
            }

            queue.push_back(vertices[target_vertex][i]);
      }
    }
    
    // max 값 counting은 vertex_value가 완성되었을 때 해야함!
    // 그 전에 하면, 유효하지 않은 큰 값이 max 값이 될 수도 있음.
    int max_value = 0;
    
    for(int i=0; i<n; i++){
        if(max_value < vertex_value[i]){
            max_value = vertex_value[i];
            answer = 1;
        }
        else if(max_value == vertex_value[i]){
            answer++;
        }
    }

    return answer;
}
