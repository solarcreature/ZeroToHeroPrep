def convert(self, s: str, numRows: int) -> str:
        
        result = [""] * numRows
        
        index, step = 0, 1
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        for char in s:
            
            result[index] += char 
            
            if index == 0:
                step = 1
            
            elif index == numRows - 1:
                step = -1
                
            index += step
            
        return "".join(result)