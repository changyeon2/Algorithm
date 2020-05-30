class Solution {
public:
   bool isPalindrome(int x) {
       if(x<0){
           return false;
        }
        std::string str = std::to_string(x);

        int stringLen = str.length();

        for(int i=0; i<(stringLen/2); i++){
            if(str[i] != str[stringLen-1-i]){
                return false;
            }
        }

        return true;    
    
    }
};
