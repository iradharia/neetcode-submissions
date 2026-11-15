"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
two interval conflict when the endA > startB
non-conflict endA <= startB
find number of conflicts and return?

1. sort the array by start time
2. create min with the end times sorted
3. while work left to do:
    if heap empty and work left to do:
        assign next task
    if tasks and time left:
        push elements on to heap
    calculate min rooms
return min rooms

"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sortedIntervals = sorted(intervals, key= lambda x: x.start)
        minHeap = []
        for i in range(len(sortedIntervals)):
            if not minHeap: # intervals left to process:
                heapq.heappush(minHeap, sortedIntervals[i].end)
                continue
            intervalEnd = minHeap[0]
            if intervalEnd > sortedIntervals[i].start:
                heapq.heappush(minHeap, sortedIntervals[i].end)
            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, sortedIntervals[i].end)
        
        return len(minHeap)





