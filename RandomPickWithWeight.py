class Solution:
    '''
    We can decide what to pick using random() and stretching it.
    When we pick from w, this is what we do:
    Get a random value.
    Scale it by sum(w).
    Iterate through w until our sum is larger. Return what makes our sum go over the scaled value.
    This is O(n) time, O(n) space.
    
    I could also keep a list that is weighted and pick from there, but that's O(sum(w)) space, O(1) time.
    '''
    def __init__(self, w: List[int]):
        self.weights = w

    def pickIndex(self) -> int:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()