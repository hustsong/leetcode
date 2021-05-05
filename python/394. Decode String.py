from string import digits, ascii_lowercase


class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        ans = ""
        
        sub_str = ""
        times = "1"
        i = 0
        while i < len(s):
            c = s[i]
            if c in digits: # get num
                curr_times = ""
                j = i
                while s[j] in digits:
                    curr_times += s[j]
                    j += 1
                i = j - 1
                if times == "1":
                    times = curr_times
                else:
                    sub_str += curr_times
            elif c == "[":
                stack.append(c)
                if len(stack) > 1:
                    sub_str += c
            elif c == "]":
                stack.pop()
                if len(stack) == 1:
                    sub_str += c
            else:
                sub_str += c

            if sub_str and not stack:
                if len(sub_str) == len(s):
                    ans += s
                else:
                    ans += int(times) * self.decodeString(sub_str)
                sub_str = ""
                times = "1"
            i += 1

        return ans


s = "3[z]2[2[y]pq4[2[jk]e2[f]]]ef"
sol = Solution()
print(sol.decodeString(s))
