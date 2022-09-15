class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low
        if low%2 == 0 and n%2 == 0:
            return n//2
        else:
            return n//2+1