#include<vector>
#include<iostream>

using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        if (len <= 1)
            return;

        int r = len - 2;
        while (r >= 0)
        {
            if (nums[r] < nums[r + 1])
            {
                // find next greater than nums[r] in nums[r + 1:]
                int swap_pos = r + 1;
                for (; swap_pos < len - 1; swap_pos++)
                {
                    if (nums[swap_pos] > nums[r] && (nums[swap_pos + 1] <= nums[r]))
                        break;
                }

                // swap
                int temp = nums[r];
                nums[r] = nums[swap_pos];
                nums[swap_pos] = temp;
                break;
            }
            r--;
        }

        // reverse vector
        int l = r + 1;
        r = len - 1;
        if (nums[l] <= nums[r])
            return;

        while (l <= r)
        {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }
};