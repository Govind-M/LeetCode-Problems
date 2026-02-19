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
    let pA = headA
    let pB = headB

    let n = 0
    while (pA) {
        n += 1
        pA = pA.next
    }

    let m = 0
    while (pB) {
        m += 1
        pB = pB.next
    }

    let diff = Math.abs(n - m)

    if (n > m) {
        let temp = headA
        headA = headB
        headB = temp
    }

    for (let i = 0; i < diff; i++) {
        headB = headB.next
    }

    pA = headA
    pB = headB

    while (pA !== pB) {
        pA = pA.next
        pB = pB.next
    }

    return pA
};