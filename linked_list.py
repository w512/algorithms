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

    def insert(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next_node = self.last
        else:
            current = Node(x, None)
            self.last.next_node = current
            self.last = current

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


if __name__ == '__main__':
    print('Linked list conception')
    print('https://en.wikipedia.org/wiki/Linked_list')

    n1 = Node(234)
    n2 = Node(1)
    n3 = Node(55)
    n4 = Node(98)
    n5 = Node(7)

    ll = LinkedList()
    ll.insert(n1)
    ll.insert(n2)
    ll.insert(n3)
    ll.insert(n4)
    ll.insert(n5)

    print()
    print(ll)
    print()

    ll.clear()
    ll.insert(n2)
    ll.insert(n5)
    ll.insert(n3)
    ll.insert(n4)
    ll.insert(n1)

    print()
    print(ll)
    print()







