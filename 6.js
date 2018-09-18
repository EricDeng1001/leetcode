// apporoach: vist by row
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  if (numRows === 1) {
    return s;
  }
  var result = '';
  var groupSize = 2 * numRows - 2;
  for (let i = 0; i < numRows; i++) {
    let visitor = i;
    while (visitor < s.length) {
      result += s[visitor];
      if ( i !== 0 && i !== numRows - 1) {
        let speicalVisitor = visitor + groupSize - 2 * i;
        if (speicalVisitor < s.length) {
          result += s[speicalVisitor];
        }
      }
      visitor += groupSize;
    }
  }
  
  return result;
};