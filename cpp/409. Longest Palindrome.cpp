#include<unordered_map>
#include<string>
#include<iostream>

using std::string;
using std::unordered_map;
using std::cout;
using std::endl;

class Solution {
public:
    int longestPalindrome(string s) {
        string::iterator s_iter = s.begin();
        unordered_map<char, int> stat;
        int even = 0;
        int odd = 0;

        while (s_iter != s.end())
        {
            if (stat.find(*s_iter) == stat.end())
            {
                stat[*s_iter] = 1;
            }
            else
            {
                stat[*s_iter]++;
            }
            s_iter++;
        }
        
        unordered_map<char, int>::iterator stat_iter = stat.begin();
        while (stat_iter != stat.end())
        {
            int count = stat_iter->second;
            if (count % 2 == 0)
            {
                even += count;
            }
            else
            {
                odd = 1;
                even += (count - 1);
            }
            stat_iter++;
        }
        
        return even + odd;
    }
};

int main(int argc, char const *argv[])
{
    string s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
    Solution sol = Solution();
    cout << sol.longestPalindrome(s) << endl;
    return 0;
}

