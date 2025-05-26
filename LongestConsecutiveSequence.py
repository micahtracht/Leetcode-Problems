from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Kinda feels dpish

        Definitely a good idea to make nums into a set
        Then I could (this is inefficient but hear me out):
        iterate through nums, and see how long of a sequence I can build.

        But that's O(n^2) worst case. Eww. I can do better.

        O(range(nums) + nlogn) also works by sorting it and checking through there.
        But range(nums) can be 2*10^9, so no. Worse than O(n^2), since n <= 1000.
        Also awful for memory.

        It's also easy to do just by sorting and iterating, but O(nlogn) is too slow.
        I need O(n).

        What if I try dp?
        Say dp[i] represents the longest sequence starting at index i.
        We'll also try ending and value.

        If we say this, then what can I do?

        Wait, first let's think of a subproblem. To make a sequence of length i,
        we need a sequence of length i-1.

        Here's how we can formulate this as a DAG:
        i connects to j iff j == i + 1
        Build a graph like that, we want the length of the longest path

        LIS was best ending at i.
        So maybe we try that.

        dp[i] represents the best sequence that ends at i.
        Let j be the index of the element of the sequence with value nums[i] - 1, if it exists.
        Then dp[i] = dp[j] + 1 or 1 if j does not exist.

        So we need to quickly find dp[j].
        Hashmap?
        Lets have a hashmap that maps values to indices. (valToIndex)

        Then we can easily build dp values.

        Okay, we have our update rule. How can we actually build dp?
        dp will have length nums, and be initialized at all 0 (or all 1).

        What value can we fix in dp?

        This is where I get stuck. So let's consider the DAG.
        I want the root of the DAG. But I can't find that easily.

        Let's come back to this later.

        Okay, later is now. You've had a day, brain, what new ideas ya got?

        Let's start with what values we can fix. Can I know if a value is the start or end
        of a sequence?

        Yes, I can. I can get the max value in O(n). (remember, O(cn) = O(n))
        So what if I fix dp[max] = 1, for starting at that.

        Wait, what if I turn nums into a set.
        Then I start at the max (takes O(n)) and decrement?
        That will become O(n + range(nums)), but something like that could work.

        Something clever that lets me not use the range.
        Sorting, of course, but that takes too long.

        Say we do this:
        Find the min and max (O(n))

        Actually, try this:
        Iterate through nums and have a list of sequences.
        If a number fits on a sequence, add it to that sequence.
        Otherwise, it becomes the start to its own sequence.

        Return the max len.

        Is that all O(n)?
        Iterating - O(n)
        Building lists - O(n)
        Checking if a number is at the top - O(1), since I can use a hashmap.

        So yes, it is O(n), and should work!

        Wait. What if I get them out of order? Then it doesn't work.
        Nevermind, then.

        Okay, I'm out of ideas. Let's try hint #1:
        Yeah yeah I know do better than n^2.

        Okay, hint 2: can we identify the start of a sequence?
        This is what I was working on.

        I could make nums a set, and for each number check if n+1 exists in nums.
        That would identify potential starts.

        Then I just iterate from every start. Still O(n^2).

        The issue is I repeat work. If I find the start of a sequence,
        I should then just call my sequence curr + len(element)

        So maybe do this:
        make nums a hashmap
        find every start, init with 1.

        Maybe I'll try the O(n^2) worst case.

        Wait, checking - 1 makes it O(n) worst case. Ugh, yeah that was the one issue.
        '''
        numSet = set()
        for i in range(len(nums)):
            numSet.add(nums[i])
        
        res = 0
        for i in range(len(nums)):
            val = nums[i]
            if val-1 not in numSet:
                count = 0
                while val in nums:
                    count += 1
                    res = max(count, res)
                    val += 1
        return res