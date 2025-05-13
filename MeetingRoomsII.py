from typing import List
class Solution:
    def minConferenceRooms(intervals: List[List[int]]) -> int:
        '''
        My first thought was to iterate over i from min interval to max and keep track of max, but that is obviously inefficient.
        
        It feels sort of sliding window-esque. Aha, maybe I do this:
        I sort all intervals by their start.
        I then iterate through all intervals and take their end and check how many intervals after start before that end.
        Repeat for every interval, and your answer is your max number of overlaps.
        Let's try it.
        
        The issue is that it counts how many overlap at one point, NOT how many are going on at once. Quite easily you could have an undercounted case.
        Also, this is O(n^2).
        
        The other common approach is two pointers. How would that work? Well, we could sort starts and ends.
        Start s, e at 0.
        Then update e as we go
        
        If s < ends[e], we need a new room. Otherwise, we can increment e. That finds the number that start before it ends.
        Because we go by what starts/ends earliest, we can advance them together, and that works.
        
        It's a sweep line problem, where we can imagine the rooms as intervals on the line, and we want to find how many overlap at once (how many intervals are active at once).
        That means sweeping over the line (hence the original approach) and seeing what works.
        In sweep line problems like this, it's common to use sorting the starts and or ends of the lists.
        That's because meeting starts and meeting ends are the ONLY times our count may change. So we can only consider them.
        
        Imagine doing it on paper: I'd put down the starts and the ends (the meetings themselves don't really matter). Then, I'd go through and see what overlaps.
        If s < ends[e] just tells me if a new room has started before an old one has opened up.
        Otherwise, we can advance our end pointer, since we want to see what'll happen with the next one.
        
        Imagine going through a schedule, seeing if ones have opened up, and when one does, knowing you can reuse it. That's what this does.
        '''
        if not intervals:
            return 0
        
        needed = 0
        starts = sorted(s for s, e in intervals)
        ends = sorted(e for s, e in intervals)
        e = 0
        
        for s in starts:
            if s < ends[e]:
                needed += 1
            else:
                e += 1
        return needed