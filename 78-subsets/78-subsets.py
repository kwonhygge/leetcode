class Solution:
    
    def subsets(self, nums):
    
        size = len(nums)
        upper_bound = 1 << size 
        
        all_subset = [ ]
        for bits_sn in range(upper_bound):
            
            cur_subset = []
            
            for i in range(size):
                
                if bits_sn & (1 << i) != 0:
                    cur_subset.append( nums[i] )
            
            all_subset.append( cur_subset )
        
        return all_subset