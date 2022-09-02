class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        
        if not nums:
            return 0
        
        newTail = 0
        
        for i in range(1,length):
            if nums[newTail]!=nums[i]:
                newTail+=1
                nums[newTail]=nums[i]
                
            
        return newTail+1
                