class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_heap = list(counts.values())
        heapq.heapify_max(max_heap)

        cooldown_queue = deque()
        time = 0

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                task_count = heapq.heappop_max(max_heap)
                task_count -= 1

                if task_count > 0:
                    cooldown_queue.append((task_count, time + n))

            if cooldown_queue and cooldown_queue[0][1] == time:
                task_count, _ = cooldown_queue.popleft()
                heapq.heappush_max(max_heap, task_count)

        return time
