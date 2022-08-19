def lengthOfLongestSubstring(self, s: str) -> int:
        
        indexMap = {}
        windowStart = 0
        maxLength = 0
        
        for windowEnd in range(len(s)):
            
            if s[windowEnd] in indexMap:
                
                windowStart = max(windowStart,indexMap[s[windowEnd]] + 1)
            
            maxLength = max(maxLength, windowEnd - windowStart + 1)
            
            indexMap[s[windowEnd]] = windowEnd
            
        return maxLength