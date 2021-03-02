#include <map>
#include <string>
#include <vector>

using namespace std;

array<int, 2> getNearestNonALetter(string name, int currentIndex, map<int, bool> isChanged){
	int nearestIndex;
	int nearestDist = name.length() + 1;
	
	for(int i=0; i<name.length(); i++){
		if(i != currentIndex && name[i] != 'A' && !isChanged[i]){
			int dist = min(abs(i-currentIndex), (currentIndex + int(name.length())- i));
			
			if(nearestDist > dist){
				nearestDist = dist;
				nearestIndex = i;
			}
		}
	}
	
	// if nearestDist is not changed, it means there is no valid next point.
	// Thus, we have return same point. (it represents 'do not move')
	if(nearestDist == name.length() + 1) return {currentIndex, 0};
	
	array<int, 2> returnArray = {nearestIndex, nearestDist};
	
	return returnArray; 
}

int solution(string name){
    int answer = 0, changeCount = 0, currentIndex = 0, toBeChangedCount = 0;
	
	map<int, bool> isChanged;
	
	// map initializing
	for(int i=0; i<name.length(); i++){
		isChanged[i] = false;
		
		if(name[i] != 'A') toBeChangedCount += 1;
	}
	
	while(changeCount < toBeChangedCount){
		answer += min((name[currentIndex] - 'A'), ('Z' - name[currentIndex] + 1));
		isChanged[currentIndex] = true;
		
		// this condition is for starting point (currentIndex == 0)
		// if starting point is equal to 'A', we don't need to include this case when calculating 'changeCount'
		if(name[currentIndex] != 'A') changeCount += 1;
		
		array<int, 2> nearestPointInfo = getNearestNonALetter(name, currentIndex, isChanged);
		
		currentIndex = nearestPointInfo[0];
		answer += nearestPointInfo[1];
	}
	
	return answer;
}
