"""
data_structures.py
Assignment 6: Elementary Data Structures
"""

# Array and Matrix Operations

class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index)

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of range")

    def __repr__(self):
        return str(self.data)


# Stack using Array

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


# Queue using Array

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete(self, key):
        cur = self.head
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if not cur:
            return  # Not found
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next

    def traverse(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(cur.data)
            cur = cur.next
        return elements

    def __repr__(self):
        return "->".join(map(str, self.traverse()))


# Example usage

if __name__ == "__main__":
    print("Array demo:")
    arr = Array()
    for i in range(5):
        arr.insert(i, i * 2)
    print(arr)
    arr.delete(2)
    print(arr)
    print("Access index 2:", arr.access(2))

    print("\nStack demo:")
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack)
    stack.pop()
    print(stack)

    print("\nQueue demo:")
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    print(queue)
    queue.dequeue()
    print(queue)

    print("\nLinked List demo:")
    ll = LinkedList()
    for i in range(5):
        ll.insert(i)
    print(ll)
    ll.delete(2)
    print(ll)
