class Solution {
public:
    int romanToInt(string s) {
        // 일반적으로 map보다 unordered map이 더 성능이 좋음!
        // https://gracefulprograming.tistory.com/3 참고
        unordered_map <char, int> m {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        
        int number = 0;
        
        for(int i=0; i<s.size(); i++){
            if(i != (s.size()-1) && m[s[i]] < m[s[i+1]]){
                number -= m[s[i]];
            }
            else{
                number += m[s[i]];
            }
        }
        
        return number;
    }
};
