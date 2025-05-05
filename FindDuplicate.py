class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Find duplicate with O(1) memory and w/o modifying nums
        Two pointers approach apparently?
        Oh, iterate two pointers through the array. If they're equal, return the duplicate.
        
        Issue: TLE
        So how do I use binary to make it faster?
        Right now my issue is I'm comparing every number to every other number: O(n^2).
        
        How does bit manipulation help me?
        Say I express every number in binary. Then what?
        I don't see how that gets me anywhere.
        
        What if I use a binary number to represent if there are duplicates? Then I run into memory issues.
        
        Pick a middle value, m. Count how many values are <= m.
        If that count exceeds m, we know which half we're in. Otherwise, check the other side.
        If equal, return m. Else, BS again.
        
        Here's the approach:
        We count the num less, and the num more. We also know the total num.
        If total - less - more = 2, then return mid.
        Else, we check if less > than the dist to mid or if more is > dist to mid.
        
        So we check:
        if less > mid
        if more > len-mid
        '''
        left, right = 1, len(nums) - 1
        while left < right: # duplicate is guaranteed
            mid = (left + right)//2 # represents the middle value by amount
            countLess = 0
            for num in nums:
                if num <= mid:
                    countLess += 1
            
            if countLess > mid:
                right = mid
            else:
                left = mid + 1
        return left # left == right == duplicate