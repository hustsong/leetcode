from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            slices = domain.split('.')
            slices.reverse()
            sub_domains = []
            for slice in slices:
                sub_domains.append(slice)
                sub_domain = '.'.join(list(reversed(sub_domains)))
                res[sub_domain] = res.get(sub_domain, 0) + int(count)
        return [' '.join([str(v), k]) for k, v in res.items()]

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]       
sol = Solution()
print(sol.subdomainVisits(cpdomains))
