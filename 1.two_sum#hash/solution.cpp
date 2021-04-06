#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> hash_table;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hash_table.find(target - nums[i]);
            if (it != hash_table.end()) {
                return {it->second, i};
            } else {
                hash_table[nums[i]] = i;
            }
        }
        return {};
    }
};

int main() {

    cout << "hello";
	vector<int> a = {1, 2, 3, 4, 5};
	Solution s = Solution();
	vector<int> res = s.twoSum(a, 6);
	for(auto i : res) {
		cout << i;
	}
	return 0;
}