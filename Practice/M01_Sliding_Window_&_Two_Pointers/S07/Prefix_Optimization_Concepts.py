'''
prefix:start from the beginning of the array element up to the current index
ex:[1,2,3,4,5]
prefix[0]=0
prefix[1]=[1,2]
prefix[2]=[1,2,3]
prefix[3]=[1,2,3,4]
prefix[4]=[1,2,3,4,5]

prefix_sum:prefix_sum[0]=0
prefix_sum[1]=1
prefix_sum[2]=1+2=3
prefix_sum[3]=1+2+3=6
prefix_sum[4]=1+2+3+4=10
prefix_sum[i]=prefix_sum[i-1]+arr[i]

why we use prefix sum?
suppose prefix :we have to calculate the sum (L,R);
without prefix:we have to calculate the sums everytime-->(o(n**2))
formula :
Sum(L,R)=prefix[R+1]-prefix[L]
diff btw
sliding window                                                    prefix
1.it contains only +ve elem                                       1.it have both +ve and -ve
2.window size is either fixed or extend and shrink                 2.exact count
'''
'''
algorithm:
1.total sum 
2,intial value of  left sum
3. traverse all array elem
4.find the right_sum
if left_sum
'''
#leetcode:724
class Solution:
    def pivotIndex(self, nums):
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            right_sum = Total_sum - Left_sum - nums[i]
            if Left_sum == right_sum:
                return i
            Left_sum += nums[i]  # Fixed from ++ to +=
        return -1
#Leetcode:1991
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Right sum is total minus left sum and current element
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
                
            left_sum += nums[i]
            
        return -1
#leetcode:1732
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
            
        return max_altitude
#leetcode:2574
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        result = []
        
        for i in range(n):
            right_sum -= nums[i]  # Update right sum by removing the current element
            result.append(abs(left_sum - right_sum))  # Calculate the absolute difference
            left_sum += nums[i]  # Update left sum by adding the current element
            
        return result