// Kruskal algorithm (C++ ver.)

// for given graph({{vertex1, vertex2, weight}}) and vertexNum(total number of vertex),

int* parent = new int[vertexNum];
	
for(int i=0; i<n; i++) parent[i] = i;
	
sort(graph.begin(), graph.end(), [](auto vec1, auto vec2) { 
	return (vec1[2] < vec2[2]);
});

int root1, root2;
int curLineNum = 0;
int cost = 0;
	
for(int i=0; i<graph.size(); i++){
	if(curLineNum == vertexNum-1) break;
		
	root1 = findFunction(graph[i][0], parent);
	root2 = findFunction(graph[i][1], parent);
	
  // 여기서 root1과 root2을 비교해야한다.
  // 그러지 않고 특정 root(root0라 하자)를 기준으로, ((root0 != root1) || (root0 != root2))로 union을 하게 된다면,
  // root0가 속해있는 tree의 vertices와 직접적으로 연결이 안 되어있는 점의 경우, mst에 포함되지 않게 된다!!
  if(root1 != root2){
		unionFunction(root1, root2, parent);
		cost += graph[i][2];
		curLineNum++;
	}
	else continue;
}
