#include <bits/stdc++.h>
using namespace std;
int V;
void add_edge(vector<vector<pair<int,int>>> &adj, char u, char v, int wt){
    u -= 'A'; v -= 'A';
    adj[u].push_back({v,wt});
    adj[v].push_back({u,wt});
}
vector<int> dijkstra(int src, vector<vector<pair<int,int>>> adj){
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    vector<int> dist(V,INT_MAX);
    pq.push({0,src}); dist[src] = 0;
    while(!pq.empty()){
        int u = pq.top().second;
        pq.pop();
        for(auto x : adj[u]){
            int v = x.first;
            int weight = x.second;
            if(dist[v] > dist[u] + weight){
                dist[v] = dist[u] + weight;
                pq.push({dist[v],v});
            }
        }
    }
    return dist;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> V >> n; //Amt of vertices and amt of edges
    vector<vector<pair<int,int> > > adj(V);
    for(int i = 0; i < n; i++){
        char u, v;
        int wt;
        cin >> u >> v >> wt; //insert n edges
        add_edge(adj, u, v, wt);
    }
    char src, dst;
    cin >> src >> dst;
    auto dist = dijkstra(src - 'A', adj);
    cout << char(dist[dst - 'A']);
}