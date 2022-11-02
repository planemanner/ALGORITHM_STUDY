import collections

class Node:
    def __init__(self, data):
        self.marked = False
        self.data = data


queue = collections.deque()
