def intToRoman(self, num: int) -> str:
        
        romansDict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        div = 1
        
        while num >= div:
            div *= 10
            
        div /= 10
        
        res = ""
        
        while num:
            
            digit = int(num / div)
            if digit <= 3:
                res += (romansDict[div] * digit)
            elif digit == 4:
                res += (romansDict[div] + romansDict[div * 5])
            elif 5 <= digit <= 8:
                res += (romansDict[div * 5] + (digit - 5) * romansDict[div])
            elif digit == 9:
                res += (romansDict[div] + romansDict[div * 10])
                
            num = num % div
            div /= 10
            
        return res