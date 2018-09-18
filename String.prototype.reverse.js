String.prototype.reverse = function(){
  let s = '';
  for (let i = this.length - 1; i >= 0; i--) {
    s += this[i];
  }
  return s;
}