class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = 0
        for i in range(0, len(nums)-2):
            tmp = nums[i:i+3]
            if max(tmp)*2 < sum(tmp):
                res = sum(tmp)
                break
        return res