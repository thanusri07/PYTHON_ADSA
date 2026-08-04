'''
sub-string:sequence of characters
ex:'thanusri'-->sub-string:'than','anus','thanu','nusr','thanu','thanu','tnu->not a sub-string
sub-sequence:skipping of characters
'''

#leetcode:3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        max_len=0
        a=set()
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left+=1
            a.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
        
# leetcode:424
'''
algorithm:
1)intialize with 0
2)take an empty dic,max_len,max_freq and assign with 0
3)move right pointer toward right(single char at a time)
4)find freaquency of each char
5)find the max_freq character
'''
#1208
