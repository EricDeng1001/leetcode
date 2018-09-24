class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        last = None
        closest = None
        min_diff = float("inf")

        i = 0
        while i < len(nums) - 2:
            if nums[i] != last:
                last = nums[i]
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    diff = sum - target

                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        closest = sum

                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return target

            i += 1

        return closest
