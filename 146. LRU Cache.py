class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.queue:
            return -1
        self.queue.move_to_end(key)
        return self.queue[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.queue:
            if len(self.queue) >= self.capacity:
                self.queue.popitem(last=False)
            self.queue[key] = value
        else:
            self.queue.move_to_end(key)
            self.queue[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
