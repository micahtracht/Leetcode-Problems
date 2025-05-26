from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Aim for O(n^2) time, O(1) space.
        So I spent ages looking for O(nlogn) for nothing. Purely wonderous.

        Well, we can do 2 sum in O(n). So do n 2 sums. Trivial.

        Here's the approach in more depth:
        Iterate through nums.
        For each index in nums, we consider all future indices (this is to preserve an 
        ordering that avoids duplicates).

        We make an array, seen, that spans from i to j. If we reach an element such
        that -1 * nums[i] + nums[j] is in seen, we have found a triplet.
        To further avoid duplicates, we can sort this triplet, make it a tuple,
        and add it to a set.

        Then we make the set into a list, and return that.

        Wait, this is O(n) space.

        Okay, let's think of something else.
        I could sort nums, since I only need the values.

        With sorted nums, is there a way to do 2-sum in O(n)?
        Yeah, with two pointers. If I'm too small, move up left. Otherwise, move down right.
        Does that work though? Or might I miss a combination?

        Let's think about it.
        Take target = 5, and:
        [2, 3, 5, 6]
        2, 6 -> 2,5 -> 2,3

        Target = 7, and:
        [1, 2, 3, 5, 8]
        1,8 -> 1, 5 -> 2, 5

        Yeah, it'll work if we start too big. What if we start too small?
        Target = 9 and:
        [1, 2, 3, 4, 5, 6]
        [1, 6] -> [2, 6] -> [3, 6]

        Tried a few different combos, seems to work. I can't make it fail.
        Maybe it does, but I can't find it. Let's roll with it.

        Okay, so sort nums (O(nlogn))
        Then iterate through every val and run 2 pointer 2 sum on the vals

        Use a set to eliminate duplicates

        Ah, what do I do about if there are multiple solutions...
        Eh, let's do it and see. Maybe something'll come to me.
        '''
        setRes = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            target = -1 * nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    listAns = [nums[i], nums[l], nums[r]]
                    listAns.sort()
                    setRes.add(tuple(listAns))
                if nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        listRes = list(setRes)
        return [list(triplet) for triplet in listRes]
                
