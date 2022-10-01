class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            sub = target - nums[i]
            ch_ls = [0] * len(nums)
            ch_ls[i] = 1
            cnt = nums[i+1:].count(sub)
            if cnt == 0:
                ch_ls[i] = 0
                continue
            elif cnt >= 1:
                idx = nums.index(sub)
                if ch_ls[idx] == 1:
                    idx = nums.index(sub, idx+1)
            return [i, idx]
