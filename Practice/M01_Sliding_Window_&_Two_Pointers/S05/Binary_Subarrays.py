'''
Binary-->It contains only 0's and 1's
ex:[1,0,1,0,1,0]
[1]
[1,0]
[1,0,1]
[0]
[0,1]
[1]
[1,1]-->not a binary sub-array
#leetcode:1493 code:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans += 1
            while ans > 1:
                if nums[left] == 0:
                    ans -= 1
                left += 1
            max_length = max(max_length, right - left)
        return max_length
#leetcode:1004 code:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans += 1
            while ans > k:
                if nums[left] == 0:
                    ans -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

        

        
'''