class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        We can find the sum of the list -> we know the duplicate.
        Oh wait, it doesn't appear exactly twice. It appears 2 or more times.

        Okay, easy to do it in O(n) space. Use a seen list.
        Yeah yeah, what could I do better?

        I can track the sum. Wait, why is this a linked list problem?
        It's not. Okay.

        So maybe we use two pointers that iterate through, fast and slow, and check if they're equal
        that works

        1, 0
        3, 1
        0, 2
        2, 3
        4, 4
        1

        Ah, I never am guaranteed it.

        Okay, so I can do it in O(n^2) easily. Let's do that first and see if it's optimal.
        
        Okay, so O(n) is possible.

        I'm reasonably confident its the fast/slow stuff.
        How do I make sure fast sees all the nodes?
        I could use two of them.

        1, 2, 3, 2, 2
        0, 1, 0

        wait, they won't always align, hence the infinite loop.
        
        Okay, what's the solution?
        Treat it as a linked list, with next[i] = nums[i]
        then run the algo
        '''
        slow, fast = nums[0], nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
                    