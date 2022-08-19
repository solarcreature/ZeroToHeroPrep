def myAtoi(self, s: str) -> int:
        
        MIN , MAX = -2 ** 31, (2 ** 31) - 1
        result, isEmpty, sign = 0, True, 1
        
        for char in s:
            
            if isEmpty:
                if char == ' ':
                    continue
                elif char == '-':
                    sign = -1
                elif char.isdigit():
                    result = int(char)
                elif char != "+":
                    return 0
                isEmpty = False
        
            else:
                if char.isdigit():
                    result = result*10 + int(char)
                    if sign * result > MAX:
                        return MAX
                    elif sign * result < MIN:
                        return MIN
                else:
                    break
                    
        return sign * result