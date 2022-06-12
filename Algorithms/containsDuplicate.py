'''
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        noDuplicatesNums = set(nums)
        
        if len(nums) > len(noDuplicatesNums):
            return True
        else:
            return False