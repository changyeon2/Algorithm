#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int findFunction(int node, int parent[]){
	if(parent[node] == node) return node; 
	 
	return parent[node] = findFunction(parent[node], parent); 
}

int unionFunction(int node1, int node2, int parent[]){
	node1 = findFunction(node1, parent); 
	node2 = findFunction(node2, parent); 

	if(node1 < node2){
		parent[node2] = node1;
		
		return node1;
	}
	else{
		parent[node1] = node2;
		
		return node2;
	}
}

int solution(int n, vector<vector<int>> costs){
	int* parent = new int[n];
	
	for(int i=0; i<n; i++) parent[i] = i;
	
	sort(costs.begin(), costs.end(), [](auto vec1, auto vec2) { 
		return (vec1[2] < vec2[2]);
	});
		
	int root1, root2;
	int lineNum = 0;
	int answer = 0;
	
	for(int i=0; i<costs.size(); i++){
		if(lineNum == n-1) break;
		
	    root1 = findFunction(costs[i][0], parent);
		root2 = findFunction(costs[i][1], parent);
		
		if(root1 != root2){
			unionFunction(root1, root2, parent);
			answer += costs[i][2];
			lineNum++;
		}
		else continue;
	}	
	
	return answer;
}
