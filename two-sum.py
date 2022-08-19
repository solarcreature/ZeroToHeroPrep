def twoSum(self, nums, target):
        
        indexMap = {}
        
        
        for i in range(len(nums)):
            
            other = target - nums[i]
            
            if other in indexMap:
                return [indexMap[other],i]
            
            else:
                indexMap[nums[i]] = i