"""Find Median from Data Stream"""
"""Link to the problem: https://leetcode.com/problems/find-median-from-data-stream/"""

import heapq


class MedianFinder:

    def __init__(self):
        """initialize your data structure here."""
        # two heaps, Large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # make sure every num small is ‹= every num in Large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    Output = medianFinder.findMedian()  # return 1.5(i.e., (1 + 2) / 2)
    print(Output)
    medianFinder.addNum(3)  # arr[1, 2, 3]
    Output = medianFinder.findMedian()  # return 2.0
    print(Output)
