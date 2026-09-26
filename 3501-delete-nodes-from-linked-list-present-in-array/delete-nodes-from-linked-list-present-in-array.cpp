class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> remove(nums.begin(), nums.end());

        // Remove nodes from the beginning
        while (head && remove.count(head->val)) {
            head = head->next;
        }

        ListNode* current = head;

        // Remove nodes from the remaining list
        while (current && current->next) {
            if (remove.count(current->next->val)) {
                current->next = current->next->next;
            } else {
                current = current->next;
            }
        }

        return head;
    }
};