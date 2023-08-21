class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        current = 1
        while(current < len(nums)):
            prev = current -1
            if nums[current] == nums[prev]:
                count = count+1
                if count > len(nums)/2:
                    return nums[current]
            else:
                count = 1
            current = current+1
        return nums[-1]
