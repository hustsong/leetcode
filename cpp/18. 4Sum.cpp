#include <vector>
#include <algorithm>
#include <iostream>

using std::vector;
using std::sort;
using std::cout;
using std::endl;

class Solution {
public:
    vector<vector<int> >fourSum(vector<int>& nums, int target)
    {   
        sort(nums.begin(), nums.end());
        vector<vector<int> > results;
        vector<int> result;
        vector<vector<int> > &rsts = results;
        vector<int> &rst = result;

        NSum(0, nums.size() - 1, 4, target, rst, rsts, nums);
        return results;
    }

    void NSum(int l, int r, int N, int target, vector<int>& result, 
                vector<vector<int> >&results, vector<int>& nums)
    {
        // stop
        if (N > (r - l + 1) || N < 2 || target < nums[l] * N || target > nums[r] * N)
            return;

        if (N == 2)
        {
            while (l < r)
            {
                int curr_sum = nums[l] + nums[r];
                if (curr_sum > target)
                {
                    r--;
                }
                else if (curr_sum < target)
                {   
                    l++;
                }
                else
                {
                    vector<int> curr_rst = result;
                    curr_rst.push_back(nums[l]);
                    curr_rst.push_back(nums[r]);
                    results.push_back(curr_rst);
                    l++;
                    while ((l < r) && (nums[l] == nums[l - 1]))
                    {
                        l++;
                    }
                }
            }
        }
        else
        {
            for (int i = l; i <= r; i++)
            {
                if (i == l || ((i > l) && (nums[i] != nums[i - 1])))
                {   
                    vector<int> new_result = result;
                    vector<int> &new_rst = new_result;
                    new_rst.push_back(nums[i]);
                    NSum(i + 1, r, N - 1, target - nums[i], new_rst, results, nums);
                }
            }
        }
    }
};


int main(int argc, char const *argv[])
{
    /* code */
    int nums_array[] = {1, 0, -1, 0, -2, 2};
    vector<int> nums(nums_array, nums_array + 6);
    vector<int> &nums_ref = nums;

    Solution sol = Solution();
    vector<vector<int> > results = sol.fourSum(nums_ref, 0);
    vector<vector<int> >::iterator iter = results.begin();

    while (iter != results.end())
    {
        vector<int>::iterator sub_iter = (*iter).begin();
        while (sub_iter != (*iter).end())
        {
            cout << *sub_iter << endl;
            sub_iter++;
        }
        
        iter++;
    }
    
    return 0;
}
