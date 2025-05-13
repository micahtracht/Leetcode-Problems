class Interval:
    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedules):
        '''
        Note: each object in schedules is a schedule object with .start and .end.
        Schedules[i] is the ith employee's schedule, schedule[i][j] is the jth interval of the ith employee. .start and .end tells us when that interval starts and ends
        
        We want to find when ALL employees aren't working. 
        
        We could iterate through each employee, and track when they aren't working. What makes that a little tricky is we have to be careful of infinity.
        But say for each employee we create intervals where they aren't working. I'll think about how to do that more, but it seems fairly doable.
        
        From here, I need to find where those intervals overlap. I want spots where every interval overlaps. But how do I do that?
        
        Wait, I don't really care about who is on free time or not. So why not merge the elements in schedules into one list of all the intervals?
        Then I can sort them by start time, and iterate through and track what's open.
        We just merge the overlapping intervals until we can't anymore. Then we can track what's open. The gaps, then, are our answer intervals.
        
        Okay, let's break this down finer so I have a better idea of what to do before I start coding:
        -For each i in schedules, make a new list, merged, that has schedules[j] appended to it. Merged is a list[tuple[schedules]], while schedules is a list[list[tuple[schedule]]].
        This is O(n).
        Then we'll take each schedule object and make it into an interval, for convenience. That's just easier to handle.
        
        So now merged is a list[tuple[int]].
        
        Now, the next big step is to merge all the intervals in merged.
        First, we sort the intervals in merge by start time (O(nlogn))
        We can merge two intervals, i and j, assuming i.start < j.start, iff:
        j.start < i.end
        Then we make a new interval, k:
        k.start = i.start, k.end = max(i.end, j.end).
        We'll delete the two intervals i and j, and replace it with k.
        
        If done correctly, this should only take one iteration, so should be O(n).
        
        Now we scan for gaps. How do we do this?
        My first thought is to iterate i from min to max, and if i is not in an interval, make a new interval with it and add to that interval until we're done.
        The intervals are nonoverlapping, so once I get over the end of one interval, I need only check the distance between the start of the next.
        Wait, that leads me to a better approach: I can just iterate over the list and take the difference between the starts and ends of each nonoverlapping list.
        
        My new interval = [i.start + 1, j.end - 1], assuming i comes right before j. Since we don't include infinity, we do this for intervals indexed 0 - len - 2.
        '''
        
        # Step 1: Merge all employees into one
        intervals = []
        for employee in schedules:
            intervals.extend(employee)
        if not intervals:
            return []
        
        # Step 2: Merge overlapping intervals
        intervals.sort(key = lambda interval: interval.start) # sort by start times, O(nlogn).
        merged = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if interval.start <= cur.end:
                cur.end = max(cur.end, interval.end)
            else:
                merged.append(cur)
                cur = interval
        merged.append(cur)
        
        
        # Step 3: Form the intervals for free time.
        res = [] # list of intervals of free time.
        for a, b in zip(merged, merged[1:]):
            res.append(Interval(a.end, b.start))
        return res
    '''
    Total time complexity: O(nlogn), dominated by sorting.
    '''

sol = Solution()
schedule = [[[1,2], [5,6]], [[1,3], [4,10]]]    
schedule2 = [[[1,3], [6,7]], [[2,4], [2,5], [9,12]]]
print(sol.findFreeTime(schedule))