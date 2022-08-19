def letterCombinations(self, digits: str):
        
        if not digits:
            return []
        
        charMap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        results = []
        
        def backtrack(i, curStr):
            
            if len(curStr) == len(digits):
                results.append(curStr)
                return
            
            for char in charMap[digits[i]]:
                backtrack(i+1,curStr + char)
        
        
        backtrack(0,"")
        
        return results