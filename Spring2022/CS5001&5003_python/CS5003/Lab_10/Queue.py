""" Align
    CS5001
    Sample code -- example of implementing the Queue ADT
"""
from collections import deque

"""
enqueue ----> queue -----> deque

adding from left
"""


class Queue:
    def __init__(self):
        self.q = deque()

    # adding element to the front queue (left)
    def enqueue(self, element):
        print(f"{str(element)} is added to the queue")
        self.q.appendleft(element)
        return

    def dequeue(self):
        try:
            print(f"{self.q[-1]} is removed from the queue")
            self.q.pop()
        except IndexError:
            print("No element in queue")

    def is_empty(self):
        is_empty = "empty" if len(list(self.q)) == 0 else "not empty"
        print(f"The queue is {is_empty}")
        return len(list(self.q)) == 0

    def peek(self):
        print(f"The element at front of the queue is {self.q[0]}")
        return self.q[0]

    def count(self):
        print(f"There are {len(self.q)} elements in the queue")
        return len(self.q)

    def __str__(self):
        result = "Queue:"
        for item in self.q:
            result += ' ' + str(item)
        return result


def main():
    q = Queue()
    q.enqueue('a')
    q.peek()
    q.enqueue('b')
    q.peek()
    q.count()
    q.enqueue('c')
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.count()
    q.is_empty()
    print(q)


if __name__ == '__main__':
    main()
