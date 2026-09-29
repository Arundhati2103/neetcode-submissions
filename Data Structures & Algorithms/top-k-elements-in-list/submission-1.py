class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of each number and store in hashmap
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        # Min heap: (frequency, number)
        minHeap = []

        for num in hashmap:
            heapq.heappush(minHeap, (hashmap[num], num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # Extract numbers
        res = []

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res
         # 1 because we need number in answer and not frequency.
        