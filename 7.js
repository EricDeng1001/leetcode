/**
 * @param {number} x
 * @return {number}
 */

String.prototype.reverse = function(){
  let s = '';
  for (let i = this.length - 1; i >= 0; i--) {
    s += this[i];
  }
  return s;
}

var reverse = function(x) {
  let sgn = '';
  if (x < 0) {
    x = -x;
    sgn = '-';
  }
  x = x.toString().reverse().replace(/^0*/, '');
  x = sgn + x;
  
  x = parseInt(x || 0);
  
  if (x > 2147483647 || x < -2147483648) {
    return 0;
  }
  
  return x;
};