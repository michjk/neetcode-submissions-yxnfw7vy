class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        self.num_map[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        idx = self.num_map[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.num_map[last] = idx
        self.nums.pop()
        del self.num_map[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()