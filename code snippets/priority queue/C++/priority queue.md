### Custom compare function
```c++
#include <queue>

auto compareFunction= [](const vector<int>& vec1, const vector<int>& vec2){
	return (vec1[1] > vec2[1]);
};

int main(){
	priority_queue<vector<int>, vector<vector<int>>, decltype(compareFunction)> minHeapBySecondElement(compareFunction);
  
	return 0;
}
```
