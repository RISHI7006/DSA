class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        stack<int> stk;  // stores indices

        for (int i = 0; i < n; i++) {
            while (!stk.empty() && temperatures[stk.top()] < temperatures[i]) {
                int prevIdx = stk.top();
                stk.pop();
                answer[prevIdx] = i - prevIdx;
            }

            stk.push(i);
        }

        return answer;
    }
};