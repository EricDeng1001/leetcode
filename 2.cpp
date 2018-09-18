/**
 * Definition for singly-linked list.
 * struct ListNode {
 *   int val;
 *   ListNode *next;
 *   ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* ptr;
    ListNode* newNode;
    ListNode* result;
    int add1, add2;
    int temp;
    bool carry;
    
    carry = false;
    temp = l1->val + l2->val;
    if (temp >= 10) {
      newNode = new ListNode(temp - 10);
      carry = true;
    } else {
      newNode = new ListNode(temp);  
    }
    ptr = result = newNode; 
    
    while(1) {
      if (l1) {
        l1 = l1->next;  
        add1 = l1 ? l1->val : 0;
      } else {
        add1 = 0;
      }
      if (l2) {
        l2 = l2->next;
        add2 = l2 ? l2->val : 0;
      } else {
        add2 = 0;
      } 
      
      if (!l1 && !l2 && carry == 0 ) {
        break;
      }
      temp = add1 + add2 + carry;
      
      carry = false;
      if (temp >= 10) {
        newNode = new ListNode(temp - 10);
        carry = true;
       } else {
        newNode = new ListNode(temp);  
      }
      ptr->next = newNode;
      ptr = newNode;
    }
    
    return result;
  }
};