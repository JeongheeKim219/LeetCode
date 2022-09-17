class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = 0
        for i in range(0, len(nums)-2):
            a, b, c = nums[i:i+3]
            if a < b+c:
                res = a+b+c
                break
        return res