class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if nums[0] != 0:
            return 0
        
        if nums[n-1] != n:
            return n
        
        for i in range(n):
            if i != nums[i]:
                return i