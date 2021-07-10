#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;

typedef struct ratio{
    ll num;
    ll den;
} ratio;

map<ll, ratio> ratioMap;
map<ll, vector<ll>> edges;
vector<bool> visited;

ll n, a, b, p, q;

ll localGcd_;

ll gcd(ll a, ll b){
    if (!a) return b;
    
    return gcd(b % a, a);
}

ll lcm(ll a, ll b){
    ll gcd_ = gcd(a, b);

    return (a / gcd_ * b);
}

void dfs(ll vertex, ratio changedVal){
    ll localGcd_ = gcd(ratioMap[vertex].num * changedVal.num, ratioMap[vertex].den * changedVal.den);
    ratioMap[vertex] = ratio{ratioMap[vertex].num * changedVal.num / localGcd_, ratioMap[vertex].den * changedVal.den / localGcd_};
    visited[vertex] = true;
    
    for(ll edgeVertex: edges[vertex]){
        if(visited[edgeVertex]) continue;
        dfs(edgeVertex, changedVal);
    }
    
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    visited = vector<bool>(n);
    
    for(int i=0; i<n-1; i++){
        cin >> a >> b >> p >> q;
        
        if(ratioMap.find(a) == ratioMap.end() && ratioMap.find(b) == ratioMap.end()){
            localGcd_ = gcd(p, q);
        
            ratioMap[a] = ratio{p / localGcd_, 1};
            ratioMap[b] = ratio{q / localGcd_, 1};
            
            edges[a] = vector<ll>();
            edges[b] = vector<ll>();
        } 
        else if(ratioMap.find(a) != ratioMap.end() && ratioMap.find(b) == ratioMap.end()){
            localGcd_ = gcd(ratioMap[a].num * q, ratioMap[a].den * p);
            
            ratioMap[b] = ratio{ratioMap[a].num * q / localGcd_, ratioMap[a].den * p / localGcd_};
            
            edges[b] = vector<ll>();
        }
        else if(ratioMap.find(a) == ratioMap.end() && ratioMap.find(b) != ratioMap.end()){
            localGcd_ = gcd(ratioMap[b].num * p, ratioMap[b].den * q);
            
            ratioMap[a] = ratio{ratioMap[b].num * p / localGcd_, ratioMap[b].den * q / localGcd_};
            
            edges[a] = vector<ll>();
        }
        else{
            fill(visited.begin(), visited.begin()+n, false);
            
            dfs(a, ratio{ratioMap[b].num * ratioMap[a].den * p, ratioMap[b].den * ratioMap[a].num * q});
        }
                
        edges[a].push_back(b);
        edges[b].push_back(a);
    }    
    
    ll lcm_ = 1, totalGcd_ = 0;
    
    for(auto it = ratioMap.begin(); it != ratioMap.end(); it++){        
        if((it->second).den != 1) lcm_ = lcm(lcm_, (it->second).den);
    }
    
    for(auto it = ratioMap.begin(); it != ratioMap.end(); it++){
        (it->second).num = ((it->second).num * lcm_) / ((it->second).den);
        (it->second).den = 1;
        
        totalGcd_ = (totalGcd_ == 0) ? (it->second).num : gcd((it->second).num, totalGcd_);
    }
    
    for(auto it = ratioMap.begin(); it != ratioMap.end(); it++){
        cout << (it->second).num / totalGcd_; 
    
        if(next(it) != ratioMap.end()) cout << " ";
        else  cout << endl;
    }
    
    cout << "";
    
    return 0;
}
