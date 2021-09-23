#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <utility>

typedef long long ll;

using namespace std;

int *segTree;

int *nums;

vector<int> answer;

int N, M;

int a, b;

int leftGoal, rightGoal;

int getSegTree(int cur, int left, int right){
    if(left == right){
        return segTree[cur] = nums[left];
    }
    
    int mid = (left + right) / 2;
    
    return segTree[cur] = min(getSegTree(2*cur + 1, left, mid), getSegTree(2*cur + 2, mid+1, right));
}

int getValue(int cur, int left, int right){
    if(left > rightGoal || right < leftGoal) return 1000000001;
    else if(left >= leftGoal && right <= rightGoal) return segTree[cur];
    else{
        int mid = (left + right) / 2;
        
        return min(getValue(2*cur + 1, left, mid), getValue(2*cur + 2, mid+1, right));
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    
    nums = new int[N];
    
    segTree = new int[1 << (int)(ceil(log2(N)) + 1)];
    
    for(int i=0; i<N; i++) cin >> nums[i];
    
    getSegTree(0, 0, N-1);
    
    for(int i=0; i<M; i++){
        cin >> a >> b;
        
        leftGoal = a-1;
        rightGoal = b-1;
        
        answer.push_back(getValue(0, 0, N-1));
    }
    
    for(int i=0; i<answer.size(); i++){
        cout << answer[i] << '\n';
    }
    
    return 0;
}
