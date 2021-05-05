# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    ...

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def bs(start, end):
            if start == end:
                return start

            pivot = int((start + end) / 2)
            if not isBadVersion(pivot):
                return bs(pivot + 1, end)
            else:
                return bs(start, pivot)

        return bs(1, n)



