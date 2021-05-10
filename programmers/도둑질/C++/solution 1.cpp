#include <string>
#include <vector>
#include <cstring>

using namespace std;

int cache[1000000][2];

int recur(int index, const bool &flag, const int &n, const vector<int> &money){
	if(flag && index >= n-1) return 0; 
	
	if(index >= n) return 0;
	
	int &ret = cache[index][(int)flag];
	if(ret != -1) return ret;
	
	ret = max(recur(index+2, flag, n, money) + money[index], recur(index+3, flag, n, money) + money[index]);
	
	return ret;
}

int solution(vector<int> money){
	memset(cache, -1, sizeof(cache));
	int n = money.size();
    
	return max(max(recur(0, true, n, money), recur(1, false, n, money)), recur(2, false, n, money));
}
