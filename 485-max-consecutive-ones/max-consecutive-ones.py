class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        c = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                max = max +1
                if (max >c):
                    c = max
            if (nums[i] == 0):
                
                max = 0
                
            
        return c

        