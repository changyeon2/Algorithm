// 보완이 필요함

typedef long long ll;

class Solution {
public:
    int myAtoi(string str) {
        ll answer = 0;
        bool isNegative = false;
        bool isNumberAppearBefore = false;
        bool isSignSet = false;
            
        for(int i=0; i < str.size(); i++){
             
            if(int(str[i]) == int('+')){
                if(isNumberAppearBefore){
                    break;
                }
                else if(isSignSet){
                    return 0;
                }
                
                isSignSet = true;
                isNumberAppearBefore = true;
            }
            else if(int(str[i]) == int('-')){
                if(isNumberAppearBefore){
                    break;
                }
                else if(isSignSet){
                    return 0;
                }
                
                isSignSet = true;
                isNegative = true;
                isNumberAppearBefore = true;
            }
            else if(int(str[i]) >= int('0') && int(str[i]) <= int('9')){
                if(!isNegative && answer*10 + int(str[i]) - 48 > INT_MAX){
                    return INT_MAX;
                }
                else if(isNegative && (answer*10 + int(str[i]) - 48) * (-1) < INT_MIN){
                    return INT_MIN;
                }
                
                answer = answer*10 + int(str[i]) - 48;
                isNumberAppearBefore = true;
            }
            else{
                 if(!isNumberAppearBefore && int(str[i]) != int(' ')){
                    return 0;
                }
                if(isNumberAppearBefore){
                   break;
                }
            }
        }
        
        if(isNegative){
            answer *= -1;
        }
        
        return answer;
    };
};
