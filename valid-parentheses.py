def isValid(self, s: str) -> bool:
        
        stack = []
        pmap = {"(":")","{":"}","[":"]"}       
        
        for char in s:
            
            if char in pmap:
                stack.append(char)
            elif len(stack) == 0 or pmap[stack.pop()] != char:
                return False
            
        return len(stack) == 0