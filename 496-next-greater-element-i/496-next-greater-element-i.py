class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res_ls = list()
        for i in range(len(nums1)):
            num = nums1[i]
            idx = nums2.index(num) + 1
            nums2_sub = nums2[idx:]
            for j in nums2_sub:
                if num < j:
                    res_ls.append(j)
                    break
            else:
                res_ls.append(-1)
                
        return res_ls