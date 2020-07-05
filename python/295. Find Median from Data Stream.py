class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.total = 0
        self.median_node = None
        self.median_node_pos = None
        self.median = None
        self.nodes = {}
        self.head = None

    class Node:
        def __init__(self, val):
            self.val = val
            self.count = 1
            self.next = None
            self.prev = None

    def addNum(self, num: int) -> None:
        self.total += 1
        if num not in self.nodes:
            new_node = self.Node(num)
            self.nodes[num] = new_node

            # insert new node
            if self.total == 1:
                self.head = new_node
            else:
                if self.head.val > num:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                else:
                    curr_node = self.head
                    while True:
                        if curr_node.next is None:
                            break
                        if curr_node.next.val > num:
                            break
                        curr_node = curr_node.next
                    new_node.next = curr_node.next
                    if curr_node.next is not None:
                        curr_node.next.prev = new_node
                    curr_node.next = new_node
                    new_node.prev = curr_node
        else:
            self.nodes[num].count += 1

        if self.total == 1:     # init
            self.median_node = self.nodes[num]
            self.median_node_pos = 0
            self.median = num
            return

        # move median_node and median_pos
        if num < self.median_node.val:   # move left
            if int(self.total % 2) == 1:
                self.median = self.median_node.val
                if num == self.median_node.val:
                    self.median_node_pos += 1
            elif int(self.total % 2) == 0:
                y = self.median
                if self.median_node_pos > 0:
                    x = y
                    self.median_node_pos -= 1
                else:
                    prev_node = self.median_node.prev
                    x = prev_node.val
                    self.median_node_pos = prev_node.count - 1
                    self.median_node = prev_node
                self.median = float((x + y) / 2)
        else:   # move right
            if int(self.total % 2) == 1:
                if self.median_node_pos < self.median_node.count - 1:
                    self.median = self.median_node.val
                    self.median_node_pos += 1
                else:
                    next_node = self.median_node.next
                    self.median = next_node.val
                    self.median_node = next_node
                    self.median_node_pos = 0
            elif int(self.total % 2) == 0:
                if self.median_node_pos < self.median_node.count - 1:
                    self.median = self.median_node.val
                else:
                    next_node = self.median_node.next
                    self.median = float((self.median_node.val + next_node.val) / 2)

    def findMedian(self) -> float:
        return self.median

    def repr(self):
        node = self.head
        while node:
            print(node.val, node.count)
            node = node.next


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(40)
print(obj.findMedian())
obj.addNum(12)
print(obj.findMedian())
obj.addNum(16)
print(obj.findMedian())
# obj.repr()
