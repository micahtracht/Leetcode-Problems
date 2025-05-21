from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Two intervals, i1 and i2, overlap iff:
        i1.start < i2.end < i1.end, or
        i2.start < i1.end < i2.end
        
        I can build the intervals list up from scratch to insert it, merging as I go according to those conditions.
        To find when I add it, I should binary search to find the index. Actually doesn't effect the O, but I want to code good solutions.
        
        Just realizing, I can eliminate my binary search and just insert newInterval the first time that I see a greater start.
        I'll try that, it's easier.
        '''
        if not intervals:
            return [newInterval]
        newIntervals = []
        inserted = False
        
        i = 0 # represents current index, in newIntervals, of what we're adding.
        while i < len(intervals) + 1:
            if not inserted:
                if i >= len(intervals) or intervals[i][0] > newInterval[0]:
                    inserted = True
                    interval = newInterval
                else:
                    interval = intervals[i]
            else:
                interval = intervals[i-1] # offset bc we inserted an interval
            
            
            if i > 0 and interval[0] <= newIntervals[-1][1]:
                # merge intervals
                toAdd = []
                toAdd.append(min(interval[0], newIntervals[-1][0]))
                toAdd.append(max(interval[1], newIntervals[-1][1]))
                newIntervals[-1] = toAdd
            else:
                newIntervals.append(interval)
            i += 1
        return newIntervals

intervals = [[1,5]]
newInterval = [2, 3]
sol = Solution()
print(sol.insert(intervals, newInterval))