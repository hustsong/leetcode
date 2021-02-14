#include<string>
#include<iostream>
#include<unordered_map>

using std::string;
using std::unordered_map;
using std::cout;
using std::endl;

class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> stat;
        string::iterator siter = s.begin();
        while (siter != s.end())
        {
            if (stat.find(*siter) == stat.end())
            {
                stat[*siter] = 1;
            }
            else
            {
                stat[*siter] += 1;
            }
            siter++;
        }
        
        int pivots = 0;
        unordered_map<char, int>::iterator stat_iter = stat.begin();
        while (stat_iter != stat.end())
        {
            int count = stat_iter->second;
            if (count % 2 == 1)
            {
                pivots++;
                if (pivots >= 2)
                {
                    return false;
                }
            }

            stat_iter++;
        }
        
        return true;
    }
};

int main(int argc, char const *argv[])
{
    string s = "aabbccde";
    Solution sol = Solution();
    cout << sol.canPermutePalindrome(s) << endl;
    return 0;
}
