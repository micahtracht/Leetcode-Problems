from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
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
