class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            current_timestamp = values[mid][0]
            current_value = values[mid][1]

            if current_timestamp == timestamp:
                return current_value
            elif current_timestamp < timestamp:
                res = current_value
                left = mid + 1
            else:
                right = mid - 1

        return res