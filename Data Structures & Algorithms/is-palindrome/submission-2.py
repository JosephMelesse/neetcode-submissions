class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s_list = [c for c in s if (c.isalpha() or c.isnumeric())]
        return s_list == s_list[::-1]
