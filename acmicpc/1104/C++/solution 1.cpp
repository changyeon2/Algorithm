#include <iostream>
#include <array>
#include <string>

using namespace std;

typedef long long ll;

bool checkZero(string S){
    for(int i=0; i<S.size(); i++){
        if(S[i] == '0') continue;
        else return false;
    }
    
    return true;
}

array<int, 2> getFrontAndBack(string S){
    int front = 0, back = 0;
    
    for(int i=0; i<S.size(); i++){
        if(S[i] == '0') front++;
        else break;
    }
    
    for(int i=S.size()-1; i>=0; i--){
        if(S[i] == '0') back++;
        else break;
    }
    
    return {front, back};
}

array<int, 2> getValidZeroSegment(string S, ll zeroCount){
    int index = 0, tempIndex = 0, tempLength = 0;
    
    for(int i=0; i<S.size(); i++){
        if(S[i] == '0'){
            if(tempLength == 0) tempIndex = i;
            
            tempLength++;
            
            if(tempLength == zeroCount){
                index = tempIndex;
                
                return {tempLength, index};
            }
            
            continue;
        }
            tempLength = 0;
    }
    
    return {0, index};
}

ll findZeroSegment(string S1, string S2, ll zeroCount){
    int S1Size = S1.size(), S2Size = S2.size();
    
    bool S1Zero = checkZero(S1), S2Zero = checkZero(S2);
    
    // case 1 : S1Zero = true, S2Zero = true
    if(S1Zero && S2Zero) return 0;
    
    int S1Front, S1Back, S2Front, S2Back;
    
    array<int, 2> frontAndBack;
    
    frontAndBack = getFrontAndBack(S1);
    S1Front = frontAndBack[0], S1Back = frontAndBack[1];
    
    frontAndBack = getFrontAndBack(S2);
    S2Front = frontAndBack[0], S2Back = frontAndBack[1];
    
    // case 2 : S1Zero = true, S2Zero = false
    if(S1Zero){
        if(zeroCount <= S1Size * 1000000 + S2Front) return 0;
        else if(zeroCount <= S2Back + S1Size * 1000000 + S2Front) return (S1Size * 1000000 + S2Size - S2Back);
        else return -1;
    }
    else{
        array<int, 2> validZeroSegment;
        
        validZeroSegment = getValidZeroSegment(S1, zeroCount);
        
        int S1Length = validZeroSegment[0], S1Index = validZeroSegment[1];
         
        // case 3 : S1Zero = false, S2Zero = true
        if(S2Zero){
            if(zeroCount <= S1Front) return 0;
            else if(zeroCount <= S1Length) return S1Index;
            else if(zeroCount <= S1Back + S1Front) return (S1Size - S1Back);
            else{
                ll S2Count = (zeroCount - 1 - S1Back - S1Front) / S2Size + 1;
                
                ll currentState = (S1Size * 1000000 * S2Count) + (S2Size * S2Count * (S2Count - 1) / 2) - S1Back;
                
                if(currentState + zeroCount > 10000000000000000LL || currentState + zeroCount < 0) return -1;
                    
                return currentState;   
            }
        }
        // case 4: S1Zero = false, S2Zero = false
        else{
            validZeroSegment = getValidZeroSegment(S2, zeroCount);
        
            int S2Length = validZeroSegment[0], S2Index = validZeroSegment[1];
            
            if(zeroCount <= S1Front) return 0;
            else if(zeroCount <= S1Length) return S1Index;
            else if(zeroCount <= S1Back + S1Front) return (S1Size - S1Back);
            else if(zeroCount <= S1Back + S2Front) return (S1Size * 1000000 - S1Back);
            else if(zeroCount <= S2Length) return (S1Size * 1000000 + S2Index);
            else if(zeroCount <= S2Back + S1Front) return (S1Size * 1000000 + S2Size - S2Back);
            else if(zeroCount <= S2Back + S2Front) return (S1Size * 1000000 * 2 + S2Size * 2 - S2Back);
            else return -1;
        }    
    }
    
    return -1;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    string S1, S2;
    ll zeroCount;
    
    cin >> S1 >> S2 >> zeroCount;
    
    cout << findZeroSegment(S1, S2, zeroCount);
}
