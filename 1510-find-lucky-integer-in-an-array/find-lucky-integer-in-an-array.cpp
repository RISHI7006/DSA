class Solution {
public:
    int findLucky(vector<int>& arr) {
        int count[501] = {0};
        for (int x : arr) count[x]++;
        for (int v = 500; v >= 1; v--)
            if (count[v] == v) return v;
        return -1;
    }
};