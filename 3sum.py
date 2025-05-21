from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sorting for 2 pointers doesn't work. Naive is O(n^3) ofc.
        I could make a set of all 2 sum values -> index (O(n^2))
        
        Instead, I could iterate through (O(n)) and reduce it to 2 sum (O(n)) which gives me net O(n^2).
        
        Can I make that faster? I can build the hashmap once, that helps a bit, but not asymptotically.
        
        I think O(nlogn) feels possible here, though. How can I do it?
        Right now, I reduce the problem to 2 sum at every location. I can solve 2sum in O(n).
        
        Let's code it and see if something better comes to mind.
        
        Let's be careful, though. Duplicates can exist, so we need to be very careful. Worst case is still n^3, since it's possible we could have n^3 solutions.
        
        This is right, but I TLE. (PROBLEM IS WIP)
        '''
        res = set() # set[list[int]]
        valToIndex = {} # val -> list[indices with that val]
        for i, num in enumerate(nums): # builds hashmap
            if num not in valToIndex:
                valToIndex[num] = []
            valToIndex[num].append(i)
        
        for i, num in enumerate(nums):
            target = -1 * num # if we can sum to that, the total sums to 0. Also, by assuming i is the first index, we avoid duplicates and make it faster (though not asymptotically)
            for j in range(i+1, len(nums)):
                if target - nums[j] in valToIndex:
                    for k in valToIndex[target - nums[j]]:
                        if k > j: # avoid duplicates, this gives us the ordering: i < j < k
                            listNums = [nums[i], nums[j], nums[k]]
                            listNums.sort()
                            res.add(tuple(listNums))

        ans = []
        for tup in list(res):
            ans.append(list(tup))
        return ans
    '''
    check if it works:
    [-1, 0, 1, 2, -1, -4]
    valToIndex: {-1: [0, 4], 0: [1], 1: [2], 2: [3], -4: [5]}
    
    target = 1
    res = []
    '''