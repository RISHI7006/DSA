class Solution {
public:
    vector<vector<int>> graph;
    vector<int> state; // 0 = unvisited, 1 = visiting, 2 = processed
    
    bool hasCycle(int course) {
        if (state[course] == 1) return true;  // back-edge -> cycle
        if (state[course] == 2) return false; // already safe
        
        state[course] = 1;
        for (int next : graph[course]) {
            if (hasCycle(next)) return true;
        }
        state[course] = 2;
        
        return false;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.assign(numCourses, {});
        state.assign(numCourses, 0);
        
        for (auto& p : prerequisites) {
            graph[p[1]].push_back(p[0]);
        }
        
        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0 && hasCycle(i)) {
                return false;
            }
        }
        
        return true;
    }
};