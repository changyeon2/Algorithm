class Solution {
    public:
        bool isMatch(string s, string p) {
            // p가 끝날 때 s도 같이 끝나야 함! (여기서 s가 더 긴 경우 체크됨)
            // 그리고 *이 아닌 이상, first_match가 false면 안 됨!(여기서 s가 더 짧은 경우'도' 체크됨)

            if(p.empty()){
                return s.empty();
                }

            bool first_match = not(s.empty()) and (p[0]==s[0] or p[0] == '.');

            if(p.size() >= 2 and p[1] == '*'){
                return isMatch(s, p.substr(2, p.size())) or 
                       (first_match and isMatch(s.substr(1, s.size()), p));
            }    
            else{
                return first_match and 
                       isMatch(s.substr(1, s.size()), p.substr(1, p.size()));
            }
        };
    };