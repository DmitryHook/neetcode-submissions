class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = [
            (count, char) for
            char, count in
            Counter(s).items()
        ]
        heapq.heapify_max(max_heap)

        result = []
        prev_count = 0
        prev_char = ''

        while max_heap:
            count, char = heapq.heappop_max(max_heap)

            result.append(char)
            count -= 1

            if prev_count > 0:
                heapq.heappush_max(
                    max_heap, (prev_count, prev_char)
                )
            
            prev_count = count
            prev_char = char

        if len(result) != len(s):
            return ''

        return ''.join(result)
