class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rvs_str_1 = str(num)[::-1]
        rvs_str_2 = str(int(rvs_str_1))[::-1]
        if num == int(rvs_str_2):
            return True
        else:
            return False
        