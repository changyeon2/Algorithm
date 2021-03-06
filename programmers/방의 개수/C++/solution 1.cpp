#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<int, vector<float>> dictionary = {
        {0, vector<float>({0, 1})},
        {1, vector<float>({1, 1})},
        {2, vector<float>({1, 0})},
        {3, vector<float>({1, -1})},
        {4, vector<float>({0, -1})},
        {5, vector<float>({-1, -1})},
        {6, vector<float>({-1, 0})},
        {7, vector<float>({-1, 1})}
    };

map<pair<float, float>, vector<bool>> visited_directions;

float current_x = 0;
float current_y = 0;

int answer = 0;

void count(int direction, float x_move, float y_move){  
    int opposite_direction = (direction + 4 > 7) ? (direction - 4) : (direction + 4);

    // check current direction to 'true'
    visited_directions[make_pair(current_x, current_y)][direction] = true;

    // get next coordinates
    float next_x = current_x + x_move;
    float next_y = current_y + y_move;

    // change current coordinates
    current_x = next_x;
    current_y = next_y;

    // if point is not visited yet
    if(visited_directions.find(make_pair(next_x, next_y)) == visited_directions.end()){             
        visited_directions[make_pair(next_x, next_y)] = vector<bool>(8, false);
        visited_directions[make_pair(next_x, next_y)][opposite_direction] = true; // check next point's direction(which will be invalid) to 'true'
    }
    // if point was visited and direction is valid for counting
    else if(visited_directions[make_pair(next_x, next_y)][opposite_direction] == false){
        visited_directions[make_pair(next_x, next_y)][opposite_direction] = true; // check next point's direction(which will be invalid) to 'true'
        answer++;
    }

    return;
}

int solution(vector<int> arrows){
    visited_directions[make_pair(0 ,0)] = vector(8, false);

    for(int i=0; i<arrows.size(); i++){
        // divide cases by arrows[i] (arrows[i] points diagonal direction when it is an odd number)
        if(arrows[i] % 2 == 1){
            count(arrows[i], dictionary[arrows[i]][0] / 2, dictionary[arrows[i]][1] / 2);
            count(arrows[i], dictionary[arrows[i]][0] / 2, dictionary[arrows[i]][1] / 2);
        }
        else{
            count(arrows[i], dictionary[arrows[i]][0], dictionary[arrows[i]][1]);
        }
    }

    return answer;
}
