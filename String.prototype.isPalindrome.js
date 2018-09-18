String.prototype.isPalindrome = function(start = 0, end = this.length - 1) {
  var mid = (end + start) / 2;
  var length = Math.floor((end - start) / 2);
  for (let i = 0; i <= length; i++) {
    if (this[Math.floor(mid + i)] !== this[(Math.ceil(mid - i))]) {
      return false;
    }
  }
  return true;
}