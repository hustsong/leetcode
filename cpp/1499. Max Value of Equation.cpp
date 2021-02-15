#include<limits>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

class Solution 
{
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        int res = numeric_limits<int>::lowest();
        vector<vector<int>> max_heap = {};
        make_heap(max_heap.begin(), max_heap.end(), less<vector<int>>());

        vector<vector<int>>::iterator point_iter = points.begin();
        while (point_iter != points.end())
        {
            // get valid top
            vector<int> top = {};
            while (true)
            {
                if ((*point_iter)[0] - max_heap[0][1] > k)
                {
                    // pop
                    pop_heap(max_heap.begin(), max_heap.end(), less<vector<int>>());
                    max_heap.pop_back();
                    continue;
                }
                top = max_heap[0];
                break;
            }
            
            // compare
            int x = (*point_iter)[0];
            int y = (*point_iter)[1];
            if (top.size() > 0)
            {
                int curr_res = x + y + top[0];
                if (curr_res > res)
                    res = curr_res;
            }

            int priority = y - x;
            vector<int> curr = {priority, x};
            max_heap.push_back(curr);
            push_heap(max_heap.begin(), max_heap.end(), less<vector<int>>());
            point_iter++;
        }

        return res;
    }
};


int main(int argc, char const *argv[])
{
    vector<vector<int>> points = {{1, 3}, {7, 0}, {5, 10}, {3, -10}};
    int k = 1;
    Solution sol = Solution();
    int res = sol.findMaxValueOfEquation(points, k);
    cout << res << endl;

    return 0;
}
