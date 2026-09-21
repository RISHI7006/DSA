class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (!head) return nullptr;
        
        head->next = removeElements(head->next, val);
        
        return (head->val == val) ? head->next : head;
    }
};