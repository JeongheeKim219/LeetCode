class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        while n > 0:
            rmd = n%10
            prod *= rmd
            summ += rmd
            n = n//10
            
        return prod - summ