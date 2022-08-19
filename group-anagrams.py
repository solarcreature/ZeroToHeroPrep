def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hMap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            
            if sortedWord not in hMap:
                hMap[sortedWord] = [word]
                
            else:
                hMap[sortedWord].append(word)
                
        return list(hMap.values())