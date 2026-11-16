class Solution {
    ListNode* cur;

    TreeNode* build(int l, int r) {
        if (l > r) return nullptr;
        int mid = l + (r - l) / 2;
        TreeNode* left = build(l, mid - 1);
        TreeNode* root = new TreeNode(cur->val);
        cur = cur->next;
        root->left = left;
        root->right = build(mid + 1, r);
        return root;
    }

public:
    TreeNode* sortedListToBST(ListNode* head) {
        int n = 0;
        for (ListNode* p = head; p; p = p->next) n++;
        cur = head;
        return build(0, n - 1);
    }
};