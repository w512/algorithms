#!/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return 'Node [{0}]'.format(self.value)


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n\t{0}\n'.format(current.value)
            while current.next_node is not None:
                current = current.next_node
                out += '\t{0}\n'.format(current.value)
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def append(self, value):
        if self.first is None:
            self.first = Node(value, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(value, None)
            self.first.next_node = self.last
        else:
            current = Node(value, None)
            self.last.next_node = current
            self.last = current

    def prepend(self, value):
        new_first = Node(value)
        new_first.next_node = self.first
        self.first = new_first

    def insert(self, position, value):
        if position == 0 or not self.first:
            self.prepend(value)
        else:
            new_node = Node(value)
            iter_node = self.first
            tmp_position = position
            while tmp_position > 1 and iter_node.next_node:
                iter_node = iter_node.next_node
                tmp_position -= 1
            new_node.next_node = iter_node.next_node
            iter_node.next_node = new_node

    def delete(self, position):
        if not self.first:
            pass
        elif position == 0:
            self.first = self.first.next_node
        else:
            iter_node = self.first
            pos = position
            while pos > 1 and iter_node.next_node:
                iter_node = iter_node.next_node
                pos -= 1
            if iter_node.next_node:
                iter_node.next_node = iter_node.next_node.next_node

    def reverse(self):
        if self.first:
            prev = None
            current = self.first
            while current:
                future = current.next_node
                current.next_node = prev
                prev = current
                current = future
            self.first = prev


if __name__ == '__main__':
    print('Linked list conception')
    print('https://en.wikipedia.org/wiki/Linked_list')

    n1 = Node(234)
    n2 = Node(1)
    n3 = Node(55)
    n4 = Node(98)
    n5 = Node(7)

    ll = LinkedList()  # []
    ll.append(n1)      # [234]
    ll.append(n2)      # [234, 1]
    ll.append(n3)      # [234, 1, 55]
    ll.append(n4)      # [234, 1, 55, 98]
    ll.append(n5)      # [234, 1, 55, 98, 7]

    print('Variant 1')
    print(ll)
    print()

    ll.clear()         # []
    ll.append(n2)      # [1]
    ll.append(n5)      # [1, 7]
    ll.append(n3)      # [1, 7, 55]
    ll.append(n4)      # [1, 7, 55, 98]
    ll.append(n1)      # [1, 7, 55, 98, 234]

    print('Variant 2')
    print(ll)
    print()

    ll.clear()         # []
    ll.append(n5)      # [7]
    ll.append(n4)      # [7, 98]
    ll.prepend(n2)     # [1, 7, 98]
    ll.append(n1)      # [1, 7, 98, 234]
    ll.insert(2, n3)   # [1, 7, 55, 98, 234]

    print('Variant 3')
    print(ll)
    print()

    ll.delete(2)   # [1, 7, 98, 234]

    print('Variant 4')
    print(ll)
    print()

    ll.insert(2, n3)   # [1, 7, 55, 98, 234]
    ll.reverse()       # [234, 98, 55, 7, 1]

    print('Variant 5')
    print(ll)
    print()
