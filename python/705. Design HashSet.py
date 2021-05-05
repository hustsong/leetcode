class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._mod = 1024
        self._buckets = [[] for _ in range(self._mod)]

    def add(self, key: int) -> None:
        hash_val = int (key % self._mod)
        if not self._buckets[hash_val]:
            self._buckets[hash_val].append(key)
        else:
            for k in self._buckets[hash_val]:
                if k == key:
                    return
            self._buckets[hash_val].append(key)

    def remove(self, key: int) -> None:
        hash_val = int (key % self._mod)
        if not self._buckets[hash_val]:
            return

        for k in self._buckets[hash_val]:
            if k == key:
                self._buckets[hash_val].remove(k)
                return

        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_val = int (key % self._mod)
        if not self._buckets[hash_val]:
            return False

        for k in self._buckets[hash_val]:
            if k == key:
                return True

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)