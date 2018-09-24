/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
  var int = parseInt(str);
  if (!int) {
    return 0;
  }
  if (int > 2147483647 ) {
    return 2147483647;
  }
  if (int < -2147483648) {
    return -2147483648;
  }
  return int;
};