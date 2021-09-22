#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits.h>

typedef long long ll;

using namespace std;

ll* segTree;

ll* nums;

vector<ll> answer;

int N, M, K;

int a, b;

ll c;

int leftGoal, rightGoal;

int goal;

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
    
    cin >> N >> M >> K;
    
    nums = new ll[N];
    
    segTree = new ll[1 << (int)(ceil(log2(N)) + 1)];
    
    for(int i=0; i<N; i++) cin >> nums[i];
    
    getSegTree(0, 0, N-1);
    
    for(int i=0; i<M+K; i++){
        cin >> a >> b >> c;
        
        if(a == 1){
            goal = b-1;
            diff = c - nums[b-1];
            
            nums[b-1] = c;
            
            update(0, 0, N-1);
        }
        else if(a == 2){
            leftGoal = b - 1;
            rightGoal = c - 1;
            
            answer.push_back(sum(0, 0, N-1));
        }
    }
    
    for(int i=0; i<answer.size(); i++){
        cout << answer[i] << endl;
    }
    
    return 0;
}
