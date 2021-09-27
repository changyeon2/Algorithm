// divide and conquer + segment tree
// O(NlogN)

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <utility>

typedef long long ll;

using namespace std;

ll *sumTree, *minTree, answer;

int *nums, N;

ll getSumTree(int cur, int left, int right){
    // O(NlogN)
    if(left == right) return sumTree[cur] = nums[left];
    
    int mid = (left + right) / 2;
    
    return sumTree[cur] = getSumTree(2*cur + 1, left, mid) + getSumTree(2*cur + 2, mid+1, right);
}

ll getMinTree(int cur, int left, int right){
    // O(NlogN)
    if(left == right){
        return minTree[cur] = nums[left];
    }
    
    int mid = (left + right) / 2;
    
    return minTree[cur] = min(getMinTree(2*cur + 1, left, mid), getMinTree(2*cur + 2, mid+1, right));
}

ll getSumValue(int cur, int left, int right, int leftGoal, int rightGoal){
    // O(logN)
    if(left > rightGoal || right < leftGoal) return 0;
    else if(left >= leftGoal && right <= rightGoal) return sumTree[cur];
    else{
        int mid = (left + right) / 2;
        
        return getSumValue(2*cur + 1, left, mid, leftGoal, rightGoal) + getSumValue(2*cur + 2, mid+1, right, leftGoal, rightGoal);
    }
}

ll getMinValue(int cur, int left, int right, int leftGoal, int rightGoal){
    // O(logN)
    if(left > rightGoal || right < leftGoal) return 1000001;
    else if(left >= leftGoal && right <= rightGoal) return minTree[cur];
    else{
        int mid = (left + right) / 2;
        
        return min(getMinValue(2*cur + 1, left, mid, leftGoal, rightGoal), getMinValue(2*cur + 2, mid+1, right, leftGoal, rightGoal));
    }
}

ll getAnswer(int leftEnd, int rightEnd){
    if(leftEnd == rightEnd){
        return (ll)nums[leftEnd] * nums[leftEnd];
    }
    else if(leftEnd > rightEnd) return 0LL;
    
    int mid = (leftEnd + rightEnd) / 2;
    
    ll temp = max(getAnswer(leftEnd, mid), getAnswer(mid+1, rightEnd));
    
    int i = mid, j = mid + 1;
    
    // divide and conquer -> O(N)
    while(i > leftEnd || j < rightEnd){
        if(i == leftEnd) j++;
        else if(j == rightEnd) i--;
        else{
            if(nums[i-1] >= nums[j+1]) i--;
            else j++;
        }
        
        temp = max(temp, getSumValue(0, 0, N-1, i, j) * getMinValue(0, 0, N-1, i, j));
    }
                       
    return temp;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    
    nums = new int[N];
    
    sumTree = new ll[1 << (int)(ceil(log2(N)) + 1)];
    minTree = new ll[1 << (int)(ceil(log2(N)) + 1)];
    
    for(int i=0; i<N; i++) cin >> nums[i];
    
    getSumTree(0, 0, N-1);
    getMinTree(0, 0, N-1);
    
    answer = getAnswer(0, N-1);
    
    cout << answer << '\n';
       
    return 0;
}
