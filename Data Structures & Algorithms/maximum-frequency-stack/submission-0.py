class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq
        if freq > self.maxFreq:
            self.maxFreq = freq
        self.group[freq].append(val)

    def pop(self) -> int:
        freq = self.maxFreq
        val = self.group[freq].pop()
        self.freq[val] -= 1
        if not self.group[freq]:
            self.maxFreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()