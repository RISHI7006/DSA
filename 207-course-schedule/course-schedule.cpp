class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> inDegree(numCourses, 0);
        
        for (auto& p : prerequisites) {
            int course = p[0], prereq = p[1];
            graph[prereq].push_back(course);
            inDegree[course]++;
        }
        
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.push(i);
        }
        
        int completed = 0;
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            completed++;
            
            for (int next : graph[course]) {
                if (--inDegree[next] == 0) {
                    q.push(next);
                }
            }
        }
        
        return completed == numCourses;
    }
};