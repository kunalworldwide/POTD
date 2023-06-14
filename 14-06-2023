import heapq

class Solution:
    def maxDiamonds(self, A, N, K):
        A = [-diamonds for diamonds in A]  # Convert to negative values for max-heap
        heapq.heapify(A)
        count = 0
        for _ in range(K):
            diamonds = -heapq.heappop(A)  # Retrieve the maximum diamonds
            count += diamonds
            heapq.heappush(A, -(diamonds // 2))  # Add the updated bag back to the heap
        return count
