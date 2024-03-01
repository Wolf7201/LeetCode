from typing import Optional


class ListNode:
    def __init__(self, value=0, next_item=None):
        self.val = value
        self.next = next_item


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    node = dummy_head
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l1 = l1.next if l1 else None

        l2_val = l2.val if l2 else 0
        l2 = l2.next if l2 else None

        column_sum = l1_val + l2_val + carry
        carry, record = divmod(column_sum, 10)
        new_node = ListNode(record)
        node.next = new_node
        node = new_node

    return dummy_head.next


def print_node_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next


def create_node_list(node_list):
    node = 0
    for i in reversed(range(len(node_list))):
        node = ListNode(node_list[i], node) if node else ListNode(node_list[i])
    return node


input_l1 = create_node_list([9, 9, 9, 9, 9, 9, 9])
input_l2 = create_node_list([9, 9, 9, 9])
# print(print_node_list(input_l1))
# print(print_node_list(input_l2))

print_node_list(addTwoNumbers(input_l1, input_l2))
