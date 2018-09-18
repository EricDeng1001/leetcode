/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  var maxStart = 0;
  var maxEnd = 0;
  var maxLength = 0;                          // use >= to check the last one
  for (let start = 0, end; start < s.length && s.length - start > maxLength; start++) {
    let i = start;
    let lastOne = s.lastIndexOf(s[start]);
    do {
      end = findNext(s, i);
      i = end;
      if (isPalindrome(s, start, end)) {
        if (end - start + 1 > maxLength) { // use >= to get the later
          maxStart = start;
          maxEnd = end;
          maxLength = end - start + 1;
        }
      }
    } while(end !== lastOne);
  }
  
  return s.slice(maxStart, maxEnd + 1);
};

function findNext(s, start) {
  var char = s[start];
  for (let i = start + 1; i < s.length; i++) {
    if (char === s[i]) {
      return i;
    }
  }
  return start;
}

function isPalindrome(s, start, end) {
  var mid = (end + start) / 2;
  var length = Math.floor((end - start) / 2);
  for (let i = 0; i <= length; i++) {
    if (s[Math.floor(mid + i)] !== s[(Math.ceil(mid - i))]) {
      return false;
    }
  }
  return true;
}