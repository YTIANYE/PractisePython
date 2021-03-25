class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            index = nums[i]
            if (0 == arr[index]):
                arr[index] += 1
            else:
                return index
