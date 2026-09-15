class Solution(object):
    def shuffle(self, nums, n):
        a = [0] * (2*n)

        for k in range(n):
            a[2*k] = nums[k]
            a[2*k +1] = nums[n+k]

        return a
        
        