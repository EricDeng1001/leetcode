class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        last = None

        i = 0
        while i < len(nums) - 2:
            if nums[i] != last:
                last = nums[i]
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum < 0:
                        j += 1
                    elif sum > 0:
                        k -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k:
                            if nums[j] == nums[j - 1]:
                                j += 1
                            if nums[k] == nums[k + 1]:
                                k -= 1

            i += 1

        return res
