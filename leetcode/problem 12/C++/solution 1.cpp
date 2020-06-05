#include <string>

// 개선 필요!

class Solution {
public:
    string intToRoman(int num) {
        string answer = "";
        
        while(num != 0){
            if(num / 900 >= 1){
                answer.append("CM");
                num -= 900;
            }
            else if(num / 400 >= 1){
                answer.append("CD");
                num -= 400;
            }
            else if(num / 90 >= 1){
                answer.append("XC");
                num -= 90;
            }
            else if(num / 40 >= 1){
                answer.append("XL");
                num -= 40;
            }
            else if(num / 9 >= 1){
                answer.append("IX");
                num -= 9;  
            } 
            else if(num / 4 >= 1){
                answer.append("IV");
                num -= 4;
            }
            else if(num / 1000 >= 1){
                num -= 1000;
                answer.push_back('M');
            }
            else if(num / 500 >= 1){
                num -= 500;
                answer.push_back('D');
            }
            else if(num / 100 >= 1){
                num -= 100;
                answer.push_back('C');
            }
            else if(num / 50 >= 1){
                num -= 50;
                answer.push_back('L');
            }
            else if(num / 10 >= 1){
                num -= 10;
                answer.push_back('X');
            }
            else if(num / 5 >= 1){
                num -= 5;
                answer.push_back('V');
            }
            else{
                num -= 1;
                answer.push_back('I');
            }
        }
        
        return answer;
        
    }
};
