class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());  // create canonical key
            groups[key].push_back(s);
        }

        vector<vector<string>> result;
        for (auto& [key, group] : groups) {
            result.push_back(group);
        }

        return result;
    }
};