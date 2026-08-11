  #Leetcode:1248
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def most(k):  #most(3) & most(3-1=2)
            if k<0:
                return 0
            left,right=0,0
            odd=0
            count=0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd+=1
                while odd>k:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count+=right-left+1
            return count
        return most(k)-most(k-1)

#Leetcode: 1763
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Base case: a nice string must have at least 2 characters
        if len(s) < 2:
            return ""
        
        # Track all unique characters in the current string
        char_set = set(s)
        
        # Scan the string to find a breaking character
        for i, char in enumerate(s):
            # If the opposite case is missing, this character is invalid
            if char.swapcase() not in char_set:
                # Divide and conquer: check the left and right substrings
                left_nice = self.longestNiceSubstring(s[:i])
                right_nice = self.longestNiceSubstring(s[i+1:])
                
                # Return the longest one (and earliest due to > comparison)
                return left_nice if len(left_nice) >= len(right_nice) else right_nice
        
        # If no invalid character is found, the whole string is nice
        return s
                