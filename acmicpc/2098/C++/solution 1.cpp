// [tsp 함수에서 cost 빼는 이유]
// 같은 flag라고 하더라도 어떤 경로를 거쳤냐에 따라 cost 값은 천차만별!
// 따라서 이 cost 값을 저장하는 것이 아닌, 현재 flag로부터 '남는 포인트들을 어떻게 거쳐야 최소가 되는지'를 저장한다!
// 즉, 과거가 아닌 미래를 보고 구한 값을 mem에 저장해야!!

// INT_MAX와 연산했을 때 overflow 조심!
// 유효하지 않은데 유효함으로 체크되는 특수 testcase 조심!

#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits.h>

using namespace std;

int n;

int w[16][16];

int mem[16][(1<<16)];

int tsp(int cur, int flag){
    int &ret = mem[cur][flag];
    
    if(ret) return ret;
    
    if(flag == (1 << n) - 1){
        if(w[cur][0] == 0) return ret = INT_MAX;
        
        return ret = w[cur][0];
    }
    
    ret = INT_MAX;
    
    int temp;
    
    for(int i=0; i<n; i++){
        if((flag & (1 << i)) || (!w[cur][i])) continue;
        
        temp = tsp(i, flag | (1 << i));
                   
        if(temp == INT_MAX) continue;
        
        ret = min(ret, w[cur][i] + temp);
    }
    
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++) cin >> w[i][j];
    }
    
    cout << tsp(0, (1 << 0)) << endl;
    
    return 0;
}
