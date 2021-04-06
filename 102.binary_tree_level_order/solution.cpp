#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector <vector <int>> ret;
        if (!root) {
            return ret;
        }

        queue <TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int currentLevelSize = q.size();
            ret.push_back(vector <int> ());
            for (int i = 1; i <= currentLevelSize; ++i) {
                auto node = q.front(); q.pop();
                ret.back().push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return ret;
    }
};

int main() {
	Solution s = Solution();


	TreeNode root(3);
	TreeNode node1(9);
	TreeNode node2(20);
	TreeNode node3(15);
	TreeNode node4(7);
	
	root.left = &node1;
	root.right = &node2;
	node1.left = &node3;
	node2.right = &node4;

	vector<vector<int>> result = s.levelOrder(&root);
	for (auto i : result) {
		for (auto j : i) {
			cout << j;
		}
	}
}