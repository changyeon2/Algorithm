#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h> 

using namespace std;

int n, k1, k2, p, q, i, reverseCount=0, checkPoint;

int lock_[500];
bool isReversed[500];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    for(i=0; i<n; i++) cin >> lock_[i];
    
    memset(isReversed, false, n);
    
    for(i=0; i<n; i++){
        if((lock_[i] - lock_[(i+1)%n] + n) % n == 1){ isReversed[i] = isReversed[(i+1)%n] = true; reverseCount++; }
        
        if(lock_[i] == 1 && lock_[(i+1)%n] == n){ checkPoint = i; }   
    }
    
    if(reverseCount == n){        
        k2 = 1;
        p = 1;
        q = n;
        k1 = (checkPoint+2) % n;
    }
    else{
        for(i=0; i<n && !isReversed[i]; i++);
        for(; i<n && isReversed[i]; i++);

        i %= n;

        k2 = n - i;

        rotate(lock_, lock_ + i, lock_ + n);

        reverse(lock_ + (n-1) - reverseCount, lock_ + n);

        p = n - reverseCount;
        q = n;

        for(i=0; i<n; i++){
            if(lock_[i] == n) k1 = n - 1 - i;
        }

        if(k1 == 0){
            k2 -= 1;
            p -= 1;
            q -= 1;
            k1 = 1;
        }

        if(k2 == 0){
            k1 -= 1;
            p += 1;
            q += 1;
            k2 = 1;
        };
    }
    
    cout << k1 << endl << p << " " << q << endl << k2 << endl;
    
    return 0;
}
