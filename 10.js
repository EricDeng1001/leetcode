// apporoach: move two cursor through s and p to match them use rules.
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
  function __isMatch(i ,j) {
    if (j >= p.length) {
       return i >= s.length;
    }
    var firstCharMatch = i < s.length && (s[i] === p[j] || p[j] === '.');
    if (p[j + 1] === '*') {
      return __isMatch(i, j + 2) || firstCharMatch && __isMatch(i + 1, j); // no match || match one
    }
    return firstCharMatch && __isMatch(i + 1, j + 1);
  }
  
  return __isMatch(0, 0);
  
};

// js solution
var isMatch = function(s, p) {
  var regExp = new RegExp('^'  + p + '$');
  return regExp.test(s);
};