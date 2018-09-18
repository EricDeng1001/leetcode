var twoSum = function(nums, target) {
  const complments = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in complments) {
      return [complments[nums[i]], i];
    } else {
      complments[target - nums[i]] = i;
    }
  }
  return [];
};