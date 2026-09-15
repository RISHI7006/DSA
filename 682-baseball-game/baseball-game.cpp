class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> stack;
        int total = 0;
        
        for (const string& op : operations) {
            if (op == "+") {
                int n = stack.size();
                int val = stack[n - 1] + stack[n - 2];
                stack.push_back(val);
                total += val;
            } else if (op == "D") {
                int val = 2 * stack.back();
                stack.push_back(val);
                total += val;
            } else if (op == "C") {
                total -= stack.back();
                stack.pop_back();
            } else {
                int val = stoi(op);
                stack.push_back(val);
                total += val;
            }
        }
        
        return total;
    }
};