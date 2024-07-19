from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_list_node_len(self, head):
        node = head
        list_node_len = 0
        while node is not None:
            list_node_len += 1
            node = node.next
        return list_node_len

    def middleNode(self, head: Optional[ListNode]):
        list_node_len = self.get_list_node_len(head)
        middle_node_index = list_node_len // 2
        node = head
        while middle_node_index > 0:
            node = node.next
            middle_node_index -= 1
        return node


class Solution2:
    def middleNode(self, head: Optional[ListNode]):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Solution3:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]


def list_node_print(list_node_head):
    if list_node_head is None:
        print("Empty List")
        return

    node = list_node_head
    while node is not None:
        print(node.val, end='')
        if node.next is not None:
            print(' -> ', end='')
        node = node.next
    print()


def list_node_create(arr):
    if not arr:
        return None

    list_node_head = ListNode(arr[0])
    current_node = list_node_head
    for i in range(1, len(arr)):
        next_node = ListNode(arr[i])
        current_node.next = next_node
        current_node = next_node
    return list_node_head


list_node_arr = [1, 1, 2]
head = list_node_create(list_node_arr)
list_node_print(head)

sol = Solution()
list_node_len = sol.get_list_node_len(head)


