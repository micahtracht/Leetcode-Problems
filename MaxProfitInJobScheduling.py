from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        Feels like something of a DP problem. So let's search for a DAG or a subproblem.
        A DAG doesn't seem obvious, so let's try subproblems.
        
        No two jobs can overlap which makes it much easier to think of techniques.
        The two patterns I'm considering are: best that starts at i, and best that ends at i.
        I'm leaning towards best that ends at i, because for the best that starts at i, going in order would give us our answer immediately, so we'd have to work backwards, and that feels odd.
        
        Just a hunch, so I'm still going to explore it:
        If we let dp[i] represent the max profit we could make starting at index i, we know dp[end] = 0.
        Our first nonzero dp value is the dp[start of the latest starting one]. Call that dp[n].
        From there, how do I find the other dp values? That's where it gets a little harder.
        
        That feels so much easier to do with dp[i] representing the best that ends at i. So let me explore that now, I can revisit best starting later:
        If dp[i] represents the best you can do, ending at index i, then:
        dp[0] = 0, and like in the case above, the first nonzero dp is dp[time when first task ends]. Call that dp[n].
        From there, dp[n+1] = what exactly?
        If I can't write a precise expression yet, let me keep reasoning on it in words.
        dp[n+1] is at least max(dp[0] through dp[n]), since we could just do nothing.
        However, for jobs starting at say index     i, dp[n+1] could be dp[i] + profit[job that starts at i]
        
        So to brute-force find dp[n], here's what I could do:
        dp[n] = max(dp[i] for i < n, and dp[j] + profit[j] for jobs that start at j and end before n)
        Still not quite sure how to implement that in a way that won't TLE given 5*10^4 lengths (it'd be O(n^2)), so let's run through an example and look for repeated work (this is example 1 from LC):
        dp = [0, 0, 0, 0, 0, 0]
        Check index 0:
        dp = [0, 0, 0, 0, 0, 0]
        By index 2:
        dp = [0, 0, 50, 50, 50, 50]
        Index 3: (10 did not influence it)
        dp = [0, 0, 50, 50, 50, 50]
        Index 4:
        dp = [0, 0, 50, 50, 90, 90]
        Index 5:
        dp = [0, 0, 50, 50, 90, 120]
        
        So that works, we get 120, but still seems inefficient.
        
        Okay, say I'm at dp[i-1]. I need to find what to do to get to dp[i]. If I'm a sentient computer, what do I do? And I'm a lazy one, so I want to do it fast.
        Aha! I'll look at a job that ends at index i, rather than considering what job to take. If I have a job, j, that ends at index i, I compute dp[i] as follows:
        dp[i] = max(dp vals, dp[start of j] + profit[j]).
        That works.
        
        Now that's still O(n^2), because I do n checks for which one ends at index j.
        It's dp, so I'm sorting the start and end times anyways. That means I can binary search for it.
        
        Okay, so here's the plan:
        dp[i] represents the best you can do ending at index i.
        To get from dp[i-1] -> dp[i], we see if there's a job ending at i, and if so, compute dp[j.start] + profit[j] and check if that's larger.
        I can also avoid the expensive max operation on all values of dp since dp must be strictly increasing, so:
        dp[i] = max(dp[i-1], dp[start[j]] + profit[j])
        
        And we find all job(s) ending at i using binary search.
        
        Let's start!
        
        I didn't actually start, so here I am reviewing for myself the next day.
        
        Approach: dp[i] represents the best you can do ending at index i.
        you search for jobs ending at i and decide whether it's worth taking
        dp[i] = max(dp[i-1], dp[j.start] + profit[j] for all jobs, j)

        This is still a little trickier though because we can't do all timesteps, that could be up to 10^8.
        So we can look at all times that jobs end, and use that instead as our times.
        We also have to sort all the lists.

        Wait, let's think more about how we index and track dp.
        dp[i] is the end of the ith job, sorted by ending date. (that's how we sorted the jobs array)
        so dp[0] = jobs[0][2], so the profit of the end of the first job.
        '''

        jobs = list(zip(startTime, endTime, profit))
        n = len(jobs)
        jobs.sort(key=lambda x: x[1]) # sort by end times so we can binary search on the end times.

        jobToIndex = {} # so we can only go through the end times in our dp array
        endTimes = [] # so we can iterate through the end times in our loop
        for i, job in enumerate(jobs):
            jobToIndex[job] = i
            endTimes.append(job[1])
        
        def findJob(endTime):
            l, r = 0, n-1
            ans = -1
            while l <= r:
                m = (l+r)//2
                if jobs[m][1] <= endTime:
                    ans = m
                    l = m + 1
                else:
                    r = m - 1
            return ans
        
        dp = [0] * (n+1)
        for i, (s, e, p) in enumerate(jobs, start=1):
            ifSkip = dp[i-1]
            prev_index = findJob(s)
            ifTake = p + (dp[prev_index + 1] if prev_index != -1 else 0)
            dp[i] = max(ifSkip, ifTake)
        return dp[n]

sol = Solution()
startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]
print(sol.jobScheduling(startTime, endTime, profit))
