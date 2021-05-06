// Find function
int findFunction(int node, int parent[]){
	if(parent[node] == node) return node; 
	 
	return parent[node] = findFunction(parent[node], parent); 
}

// union function
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
