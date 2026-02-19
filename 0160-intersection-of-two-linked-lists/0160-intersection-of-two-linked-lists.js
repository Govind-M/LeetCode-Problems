/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
    let curr1 = headA
    let curr2 = headB
    let lookup = new Set()
    while (curr2 != null) {
        lookup.add(curr2)
        curr2 = curr2.next
    }
    while (curr1 != null) {
        if (lookup.has(curr1)) {
            return curr1
        }
        curr1 = curr1.next
    }
    return null
};