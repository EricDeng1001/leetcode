class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complments = {}
        for i in range(len(nums)):
            if nums[i] in complments:
                return [complments[nums[i]], i]
            else:
                complments[target - nums[i]] = i
                
        return []