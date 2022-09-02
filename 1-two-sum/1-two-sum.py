class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        
        for index, num in enumerate(nums):
            rest = target-num
            
            if rest in num_dic:
                return [index,num_dic[rest]]
            else:
                num_dic[num] = index
                
        return []
        
        