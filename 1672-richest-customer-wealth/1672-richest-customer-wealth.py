class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for ls in accounts:
            if maxi < sum(ls):
                maxi = sum(ls)
        return maxi