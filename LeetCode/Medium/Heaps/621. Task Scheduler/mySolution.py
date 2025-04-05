class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks) # O(n)
        max_heap = []

        for freq in frequency.values():
            max_heap.append(-freq)

        heapq.heapify(max_heap) # O(n)

        wait_queue = deque()
        time = 0

        while max_heap or wait_queue: # O(n)
            time+=1

            if max_heap:
                current_task = heapq.heappop(max_heap)
                current_task+=1

                if current_task!=0:
                    wait_queue.append((current_task, time+n))
            
            if wait_queue and wait_queue[0][1]==time:
                heapq.heappush(max_heap, wait_queue.popleft()[0])
            
        return time
