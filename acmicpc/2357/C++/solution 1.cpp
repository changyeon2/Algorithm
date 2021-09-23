// '\n' is much faster than std::endl
// (because '\n' does not contain a flush operation)

#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <utility>

typedef long long ll;

using namespace std;

int *maxTree, *minTree;

int *nums;

vector<pair<int, int>> answer;

int N, M;

int a, b;

int leftGoal, rightGoal;

int getSegTree(int cur, int left, int right, bool sign){
    if(left == right){
        if(sign) return maxTree[cur] = nums[left];
        else return minTree[cur] = nums[left];
    }
    
    int mid = (left + right) / 2;
    
    // bool sign
    // true -> maxSegTree
    // false -> minSegTree
    
    if(sign) return maxTree[cur] = max(getSegTree(2*cur + 1, left, mid, sign), getSegTree(2*cur + 2, mid+1, right, sign));
    else return minTree[cur] = min(getSegTree(2*cur + 1, left, mid, sign), getSegTree(2*cur + 2, mid+1, right, sign));
}

int getValue(int cur, int left, int right, bool sign){
    if(left > rightGoal || right < leftGoal) return (sign ? 0 : 1000000001);
    else if(left >= leftGoal && right <= rightGoal) return (sign ? maxTree[cur] : minTree[cur]);
    else{
        int mid = (left + right) / 2;
        
        return (sign ? max(getValue(2*cur + 1, left, mid, sign), getValue(2*cur + 2, mid+1, right, sign)) : min(getValue(2*cur + 1, left, mid, sign), getValue(2*cur + 2, mid+1, right, sign)));
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    
    nums = new int[N];
    
    maxTree = new int[1 << (int)(ceil(log2(N)) + 1)];
    minTree = new int[1 << (int)(ceil(log2(N)) + 1)];
    
    for(int i=0; i<N; i++) cin >> nums[i];
    
    getSegTree(0, 0, N-1, true);
    getSegTree(0, 0, N-1, false);
    
    for(int i=0; i<M; i++){
        cin >> a >> b;
        
        leftGoal = a-1;
        rightGoal = b-1;
        
        answer.push_back({getValue(0, 0, N-1, false), getValue(0, 0, N-1, true)});
        
    }
    
    for(int i=0; i<answer.size(); i++){
        cout << answer[i].first << " " << answer[i].second << '\n';
    }
    
    return 0;
}
