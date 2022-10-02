class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res_ls = list()

        for point in range(len(nums)-2):
            
            if point > 0 and nums[point] == nums[point-1]:
                continue
            
            lt, rt = point + 1, len(nums) - 1
            while lt < rt:
                if lt == point:
                    lt += 1
                if rt == point:
                    rt -= 1
                if point != lt and point != rt and rt != lt:
                    tot = nums[point] + nums[rt] + nums[lt]
                    if tot > 0:
                        rt -= 1
                    elif tot < 0:
                        lt += 1
                    else:
                        res_ls.append((nums[point], nums[rt], nums[lt]))
                        while lt < rt and nums[lt] == nums[lt + 1]:
                            lt += 1
                        while lt < rt and nums[rt] == nums[rt - 1]:
                            rt -= 1
                        lt += 1
                        rt -= 1
                    
        return res_ls
