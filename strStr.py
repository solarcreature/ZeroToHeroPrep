def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        if not haystack or len(haystack) < len(needle):
            return -1
        
        
        for i in range(len(haystack) - len(needle) + 1):
            
            for j in range(len(needle)):
                if (haystack[i + j]) != needle[j]:
                    break
                
            
            if haystack[i] == needle[0] and needle[j] == haystack[i + j]:
                
                return i
                
            
        return -1