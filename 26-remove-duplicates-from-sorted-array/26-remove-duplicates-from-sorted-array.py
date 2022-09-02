class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        
        for index in range(1, len(nums)):
            if nums[index] != curr:
                curr = nums[index]
                nums[count] = curr
                count += 1
        
        return count
                