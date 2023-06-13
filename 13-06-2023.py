import heapq
class Solution:

    def kLargest(self,arr, n, k):
        min_heap = []
        result = []
    
        # Insert first K elements into the min-heap
        for i in range(k):
            heapq.heappush(min_heap, arr[i])
    
        # Process remaining elements
        for i in range(k, n):
            if arr[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, arr[i])
    
        # Extract elements from min-heap in decreasing order
        while min_heap:
            result.append(heapq.heappop(min_heap))
    
        return result[::-1]
