#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int, int> nums_map;
        for (int i = 0; i < nums.size(); i++)
        {
            int curr = nums[i];
            int diff = target - curr;
            if (nums_map.find(diff) != nums_map.end())
            {
                result.push_back(nums_map[diff]);
                result.push_back(i);
                break;
            }
            
            nums_map[curr] = i;
        }

        return result;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol = Solution();
    vector<int> nums = {1, 2, 3};
    return 0;
}
