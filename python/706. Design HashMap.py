class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._mod = 1024
        self._buckets = [[] for _ in range(self._mod)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_val = int (key % self._mod)
        if not self._buckets[hash_val]:
            self._buckets[hash_val].append([key, value])
        else:
            for i, kv in enumerate(self._buckets[hash_val]):
                if kv[0] == key:
                    self._buckets[hash_val][i][1] = value
                    return
            self._buckets[hash_val].append([key, value])
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_val = int (key % self._mod)
        if not self._buckets[hash_val]:
            return -1

        for kv in self._buckets[hash_val]:
            if kv[0] == key:
                return kv[1]

        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_val = int (key % self._mod)
        if not self._buckets[hash_val]:
            return

        for _, kv in enumerate(self._buckets[hash_val]):
            if kv[0] == key:
                self._buckets[hash_val].remove(kv)
                return

        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
param_2 = obj.get(1)
obj.remove(1)