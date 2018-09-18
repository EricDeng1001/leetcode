/*
思路:
选择合适的数把两个数列分别拆分为左右部分，
对于偶数：两个左边部分加起来等于两个右边部分，
此时左边部分的最大值和右边部分的最小值一定是中位数。
对于奇数：
两个左边部分和两个右边部分的差值为1，多的那边的最值为中位数

选择的数字从小列中选取，然后从大列中割取数量相补的左列填补，这样就保证了左列和右列相等(或者右边多一个，这样右边的最小值就是中位数),
需要做的就是保证这个数值的确是中位数，那么只需要其左边的最大数字比右边的最小数字小即可。
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  if (nums1.length < nums2.length) {
    let tmp = nums1;
    nums1 = nums2;
    nums2 = tmp;
  }
  
  const m = nums1.length;
  const n = nums2.length;
  
  var left = 0;
  var right = n;
  var i, j;
  var leftMax;
  var rightMin;
  var lefted = false;
  
  for (let x = 0; x < 100; x++) {
    // left part: nums2[0..i-1] with nums1[0..j-1] length i + j
    // right part: nums2[i...n-1] with nums1[j...m-1] length n - i + m - j
    i = Math.floor((left + right) / 2);
    if (n === 1) {
      if (lefted) {
        i = 1;
      }
      lefted = true;
    }
    j = Math.floor((m + n + 1) / 2 - i); // i + j === m - i + n -j + 1;
    
    leftMax = Math.max(nums2[i - 1] || -Infinity, nums1[j - 1] || -Infinity);
    rightMin = Math.min(nums2[i] || Infinity, nums1[j] || Infinity);
    console.log(lefted, leftMax, rightMin, i, j);
    if (leftMax <= rightMin) {
      break;
    } else {
      if (left === right) {
        break;
      }
      if (nums1[j - 1] > nums2[i]) {
        // should increase i
        left = i + 1;
      } else {
        right = i - 1;
      }
    }
  }
  if ((m + n) & 1) {
    return leftMax;
  } else {
    return (rightMin + leftMax) / 2;
  }
  
};