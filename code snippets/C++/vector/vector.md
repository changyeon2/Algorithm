#### Get max value of vector
```C++
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> vec1{1, 2, 3};
    int maxValue = *max_element(vec1.begin(), vec1.end());
}
```
