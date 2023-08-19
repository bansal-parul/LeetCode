class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0
        for i in range(0,len(nums)):
            current = max(current-1,nums[i])
            if current + i >= len(nums)-1:
                return True
            if current <=0:
                return False
        return True
