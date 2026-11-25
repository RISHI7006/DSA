class Solution {
    private ListNode merge(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (a != null && b != null) {
            if (a.val <= b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }
            tail = tail.next;
        }
        tail.next = (a != null) ? a : b;
        return dummy.next;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        if (n == 0) return null;

        for (int step = 1; step < n; step *= 2) {
            for (int i = 0; i + step < n; i += step * 2) {
                lists[i] = merge(lists[i], lists[i + step]);
            }
        }
        return lists[0];
    }
}