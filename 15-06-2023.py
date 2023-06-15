class Solution:
    def longestPalin(self, s):
        longest_palindrome = ""
        max_length = 0
        
        if s == s[::-1]:
            return s
        
        for i in range(len(s)):
            current_palindrome = ""
            current_length = 0
            
            for j in range(i, len(s)):
                current_palindrome += s[j]
                current_length += 1
                
                if current_palindrome == current_palindrome[::-1]:
                    if current_length > max_length:
                        longest_palindrome = current_palindrome
                        max_length = current_length
                        
        return longest_palindrome
