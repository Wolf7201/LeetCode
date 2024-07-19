class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_from_end(self):
        if self.tail is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def remove_from_front(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def move_left(self, node):
        if node.prev is None:
            return
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node

        node.prev = node.next = None

        self.add_to_front(node)

    def move_right(self, node):
        if node.next is None:
            return
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node

        node.prev = node.next = None

        self.add_to_end(node)

    def get_string(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += current_node.value
            current_node = current_node.next
        return result


def main():
    final = input()
    s = input()

    linked_list = LinkedList()
    for char in final:
        linked_list.add_to_end(char)

    i = 0
    while i < len(s):
        if s[i] == '<':
            # left
            if s[i:i + 6] == '<left>':
                linked_list.move_left(linked_list.tail)
                i += 6
            # right
            elif s[i:i + 7] == '<right>':
                linked_list.move_right(linked_list.head)
                i += 7
            # bspace
            elif s[i:i + 8] == '<bspace>':
                linked_list.remove_from_end()
                i += 8
            # delete
            elif s[i:i + 8] == '<delete>':
                linked_list.remove_from_front()
                i += 8
        else:
            linked_list.add_to_end(s[i])
            i += 1

    if linked_list.get_string() == final:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()