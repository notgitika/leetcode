'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        
        for i in range(len(nums)):
        
            if target == int(nums[i]):
                index = i
                break
        
        return index
    
    
    """
    # Using binary search
    
    i = 0
    j = len(nums) - 1
    
    while(i<=j):
        mid = (i+j)//2
        if target < nums[mid]:
            j = mid - 1
            
        elif target > nums[mid]:
            i = mid + 1
            
        else:
            return mid
            
    return -1
    
    
    """