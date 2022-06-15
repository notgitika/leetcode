"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        else:
            temp = x
            res = 0
            
            while temp > 0:
                res = res * 10 + temp % 10
                temp //= 10
                
            if x == res:
                return True
            else:
                return False