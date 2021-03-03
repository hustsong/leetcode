import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c in string.ascii_letters + string.digits]).lower()
        return s == s[::-1]


s = "aaa"
sol = Solution()
print(sol.isPalindrome(s))
