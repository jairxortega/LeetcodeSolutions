class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # initialize an empty hashset

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
# Time complexity: O(n)
# The run time is O(n) because we are only iterating through the nums list once.
# Space complexity: O(n)
