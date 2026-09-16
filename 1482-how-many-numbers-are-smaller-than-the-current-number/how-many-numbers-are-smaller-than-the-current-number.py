class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        out = []
        i = 0
        j=0
        for i in range(n):
            count = 0
            for j in range(n):
                if (nums[i] > nums[j]):
                    count = count + 1
            out.append(count)

        return out



        