class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ls = [x for x in s.upper() if x.isalnum()]
        return s_ls == s_ls[::-1]
        