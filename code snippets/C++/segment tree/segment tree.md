#### Segment Tree (C++ Ver.)
```C++
// indices start from 0, thus index of child node is 2*idx + 1, 2*idx + 2 respectively. (instead of 2*idx, 2*idx + 1)

#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits.h>

typedef long long ll;

using namespace std;

ll* segTree, nums;

vector<ll> answer;

int N, leftGoal, rightGoal, goal;

ll diff;

ll getSegTree(int cur, int left, int right){
    if(left == right) return segTree[cur] = nums[left];
    
    int mid = (left + right) / 2;
    
    return segTree[cur] = getSegTree(2*cur + 1, left, mid) + getSegTree(2*cur + 2, mid+1, right);
}

ll sum(int cur, int left, int right){
    if(left > rightGoal || right < leftGoal) return 0;
    else if(left >= leftGoal && right <= rightGoal) return segTree[cur];
    else{
        int mid = (left + right) / 2;
        
        return sum(2*cur + 1, left, mid) + sum(2*cur + 2, mid+1, right);
    }
}

void update(int cur, int left, int right){
    if(goal < left || goal > right) return;
    
    segTree[cur] += diff; 
    
    if(left != right){
        int mid = (left + right) / 2;
        
        update(2*cur + 1, left, mid);
        update(2*cur + 2, mid+1, right);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    
    nums = new ll[N];
    
    segTree = new ll[1 << (int)(ceil(log2(N)) + 1)];
    
    for(int i=0; i<N; i++) cin >> nums[i];
    
    getSegTree(0, 0, N-1);
    
    return 0;
}
```
