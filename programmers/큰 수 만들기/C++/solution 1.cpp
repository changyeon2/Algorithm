#include <string>
#include <vector>

using namespace std;

string solution(string number, int k){
    string answer = "";
    int theBiggestNumberIndex, curIndex = 0;

    int count = number.length() - k;

    while(count != 0){
        theBiggestNumberIndex = curIndex;

        for(int i=curIndex; i<number.length()-count+1; i++){
            if(number[theBiggestNumberIndex] < number[i]) theBiggestNumberIndex = i;

            if(number[theBiggestNumberIndex] == '9') break;
        }

        answer.push_back(number[theBiggestNumberIndex]);

        count -= 1;
        curIndex = theBiggestNumberIndex + 1;
    }

    return answer;
}
