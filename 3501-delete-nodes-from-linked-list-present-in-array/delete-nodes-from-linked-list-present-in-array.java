class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        HashSet<Integer> remove = new HashSet<>();

        for (int num : nums) {
            remove.add(num);
        }

        // Remove nodes from the beginning
        while (head != null && remove.contains(head.val)) {
            head = head.next;
        }

        ListNode current = head;

        // Remove remaining nodes
        while (current != null && current.next != null) {
            if (remove.contains(current.next.val)) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}