class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        straight = []
        backward = []
        for i in range(0, len(nums)-1):
            product = product*nums[i]
            straight.append(product)
        product = 1
        len_nums = len(nums)
        for i in range(0, len(nums)-1):
            product = product*nums[-(i+1)]
            backward.append(product)
        ans = []
        for i in range(0, len(nums)):
            if i == 0:
                ans.append(backward[-1])
                continue
            elif i == len_nums-1:
                ans.append(straight[-1])
            else:
                prod = straight[i-1]*backward[-(i+1)]
                ans.append(prod)
        return ans
            





        
        
