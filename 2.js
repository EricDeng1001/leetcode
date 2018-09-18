/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  var carry = false;
  var head = new ListNode();
  var ptr = head;
  while (l1 || l2 || carry) {
    let right = l2 ? l2.val : 0;
    let left = l1 ? l1.val : 0;
    var value = right + left + carry;
    carry = false;
    if (value >= 10) {
      value -= 10;
      carry = true;
    }
    let newNode = new ListNode(value);
    ptr.next = newNode;
    ptr = newNode;
    l1 = l1 && l1.next;
    l2 = l2 && l2.next;
  }
  
  return head.next;
};