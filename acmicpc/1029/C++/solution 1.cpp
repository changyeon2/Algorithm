#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int n;

array<array<int, 15>, 15> lines;

int dp[15][(1<<15)][10];

int dfs(int cur, int flag, int price, int count){
    int &ret = dp[cur][flag][price];
    
    if(ret) return ret;
    
    ret = count;
    
    for(int i=0; i<n; i++){
        if((flag & (1 << i)) || lines[cur][i] < price) continue;
                
        ret = max(ret, dfs(i, (flag | (1 << i)), lines[cur][i], count+1));
    }
    
    return ret;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    char* temp = new char[n];
    
    for(int i=0; i<n; i++){
        cin >> temp;
        
        for(int j=0; j<n; j++) lines[i][j] = temp[j] - 48;
    }
    
    cout << dfs(0, 1, 0, 1) << endl;
    
    return 0;
}
