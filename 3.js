/**
 * @param {string} s
 * @return {number}
 */ 
/*
left      right
  |        |
  xabcdefgwx
left points to longest string's first char's -1 and right point to the last char
*/


var lengthOfLongestSubstring = function(s) {
  const charTable = {};
  var maxLength = 0;
  var char;
  for (let left = -1, right = 0; right < s.length; right++) {
    char = s[right];
    if (char in charTable) {
      left = Math.max(left, charTable[char]);
    }
    charTable[char] = right;
    maxLength = Math.max(maxLength, right - left);
  }
  return maxLength;
};