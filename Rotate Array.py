class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = [0]*len(nums)
        size = len(nums)
        for i in range(size):
            new_pos = (i+k)%size
            l[new_pos] = nums[i]
        for i in range(size):
            nums[i] = l[i]
