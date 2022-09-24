class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[1::2] = sorted(nums[1::2], reverse = True)
        nums[::2] = sorted(nums[::2])
        return nums