'''
Given a string s, reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        newWords = list()
        
        for word in words:
            newWord = word[::-1]
            newWords.append(newWord)
            
        result = " ".join(newWords)
        return result
        
    # print(reverseWords("Let's take LeetCode contest"))