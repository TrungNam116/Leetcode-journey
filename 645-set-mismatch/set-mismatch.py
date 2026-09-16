class Solution(object):
    def findErrorNums(self, nums):
        duplicate = 0
        seen = set()
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        expect_sum = len(nums) * (len(nums) + 1) /2   
        missing_num = expect_sum - (sum(nums) - duplicate)
        return [duplicate, missing_num] 

            