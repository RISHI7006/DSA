/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> visited;
    
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        // If already cloned, return the existing clone (avoids infinite loop)
        if (visited.count(node)) {
            return visited[node];
        }
        
        // Create clone and register it BEFORE recursing into neighbors
        Node* clone = new Node(node->val);
        visited[node] = clone;
        
        // Recursively clone all neighbors and attach them
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(cloneGraph(neighbor));
        }
        
        return clone;
    }
};