class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return height(root) != -1;
    }

private:
    int height(TreeNode* node) {
        if (node == nullptr) return 0;

        int leftH = height(node->left);
        if (leftH == -1) return -1; // left subtree already unbalanced

        int rightH = height(node->right);
        if (rightH == -1) return -1; // right subtree already unbalanced

        if (abs(leftH - rightH) > 1) return -1; // this node is unbalanced

        return max(leftH, rightH) + 1;
    }
};