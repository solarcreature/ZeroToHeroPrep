def threeSumClosest(self, nums, target):
        
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        
        for i in range(len(nums)):
            
            l, r = i + 1, len(nums) - 1 
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if threeSum == target:
                    return threeSum
                
                if abs(threeSum - target) < abs(result - target):
                    result = threeSum
                    
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
        return result