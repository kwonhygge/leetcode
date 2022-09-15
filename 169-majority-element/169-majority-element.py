class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        halfOfLen = len(nums) // 2
        
        for key,value in dic.items():
            if value > halfOfLen:
                return key