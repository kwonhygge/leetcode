import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "[^a-zA-Z0-9]"
    
        
        newStr = re.sub(pattern,'',s).lower()
        
        return newStr == newStr[::-1]