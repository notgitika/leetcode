'''
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. If not, return the 
    index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        i = 0
        j = length - 1

        while i <= j:
            mid = (i + j ) // 2

            if target in nums:
                return nums.index(target)

            if nums[mid] < target:
                i = mid + 1

            else:
                j = mid - 1
        return i
            