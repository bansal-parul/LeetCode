class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        if len(nums) == 0:
            return 0
        new_list.append(nums[0])
        current = 1
        count = 1
        while(current != len(nums)):
            prev = current -1
            if nums[current] == nums[prev]:
                if count <2:
                    new_list.append(nums[current])
                current = current+1
                count = count+1
            else :
                new_list.append(nums[current])
                current = current+1
                count = 1
        for i in range(len(new_list)):
            nums[i] = new_list[i]
        return len(new_list)
