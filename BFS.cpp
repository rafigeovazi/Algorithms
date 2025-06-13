#include <iostream>
#include <list>
#include <queue>
#include <vector>

using namespace std;

class Graph {
    int V;
    vector<list<int>> adj;

public:
    Graph(int V) {
        this->V = V;
        adj.resize(V);
    }

    void addEdge(int v, int w) {
        adj[v].push_back(w);
        adj[w].push_back(v);
    }

    void BFS(int startVertex) {
        vector<bool> visited(V, false);
        queue<int> queue;

        visited[startVertex] = true;
        queue.push(startVertex);

        while (!queue.empty()) {
            int currentVertex = queue.front();
            cout << currentVertex << " ";
            queue.pop();

            for (auto i = adj[currentVertex].begin(); i != adj[currentVertex].end(); ++i) {
                if (!visited[*i]) {
                    visited[*i] = true;
                    queue.push(*i);
                }
            }
        }
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);

    cout << "Breadth-First Search starting from vertex 0:\n";
    g.BFS(0);

    return 0;
}
