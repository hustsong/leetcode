class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        left_vowels, right_vowels = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while left < right:
            if s[left] in vowels:
                left_vowels += 1
            if s[right] in vowels:
                right_vowels += 1

            left += 1
            right -= 1

            if abs(left_vowels - right_vowels) > (len(s) / 2 - left):
                return False


        return True if left_vowels == right_vowels else False

