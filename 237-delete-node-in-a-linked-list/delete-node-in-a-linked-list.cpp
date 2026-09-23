/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        // Copy the value from the next node into this node
        node->val = node->next->val;
        // Skip over the next node, effectively "deleting" it
        ListNode* temp = node->next;
        node->next = node->next->next;
        delete temp; // free the memory of the now-bypassed node
    }
};