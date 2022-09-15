class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        answer = []
        
        for i in range(numRows):
            listWithOnes = []
            
            for j in range(i+1):
                listWithOnes.append(1)
            
            answer.append(listWithOnes)
            
        for i in range(numRows):
            for k in range(i-1):
                answer[i][k+1] = answer[i-1][k] + answer[i-1][k+1]
                    
        return answer