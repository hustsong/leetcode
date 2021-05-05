class MaxStack(list):

    def __init__(self):
        """
        initialize your data structure here.
        """
        ...

    def push(self, x: int) -> None:
        if len(self) == 0:
            return self.append((x, x))

        max_ele = x if x > self[-1][1] else self[-1][1]
        self.append((x, max_ele))

    def pop(self) -> int:
        return list.pop(self)[0]

    def top(self) -> int:
        return self[-1][0]

    def peekMax(self) -> int:
        return self[-1][1]

    def popMax(self) -> int:
        max_ele = self[-1][1]
        bak = []
        while self[-1][0] != max_ele:
            bak.append(self.pop())

        # pop top-most max
        self.pop()
        for ele in bak[::-1]:
            self.push(ele)
        return max_ele
        

# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(5)
obj.push(1)
print(obj.popMax())
print(obj.peekMax())

