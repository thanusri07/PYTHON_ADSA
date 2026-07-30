'''
Sliding Window:
2 types
1.Fixed-->size of the window in always fixed
2.variable

2.variable sliding window:
--> size of the window is not fixed
-->either may be increase or decrease based upon the condition
ex:[2,1,5,8,39]                  fixed:k=3
                                 [2,1,5]-->[1,5,8]-->[5,8,39]
[2]
[2,1]
[2,1,5]
[2,1,5,8]
[1,5]
[1,5,8]
-------
-------
-------
Real-world application:
meesho product purchase app


Algorithm for variable sliding window:
step-1:Two-pointer approach
step-2:for loop
step-3:expand the window
step-4:check with condition
step-5:if condition is false
step-6:shrink the window
step-7:update the result/answer



How to identify,which type of sliding window will be used in problem-solving:
sliding window concepts are mainly used in sub-arrays or sub-strings

Fixed:                                                    variable
1.Size of k                                               1.Atmost of k
2.Length of k                                             2.almost of k
                                                           3.Minimum or maximum of k
                                                           4.less than or equal & greater than or equal to k
'''    
#Find the longest sub-array with sum is less or equal to k?
# arr=[2,3,1,4,2]
# k=6

# logic:
# [2]-->2<=6(T)                 length:1
# expand[2,3]-->2+3=5<=6(T)     length=2
# expand[2,3,1]-->2+3+1=6<=6(T)   length=3
# expand[2,3,1,4]-->2+3+1+4=10<6(f)
# shrink[3,1,4]-->3+1+4=8<=6(f)   
# shrink[1,4]-->1+4=5<=6(T)      length=2
# expand[1,4,2]-->1+4+2=7<=6(f)
# shrink[4,2]=4+2=6<=6(T)         length=2
# max(1,2,3,2,2)=3
'''
def longest(arr,k):
    left=0
    right=0
    add=0
    max_len = float('-inf')                     #min_len=float('inf)
    for right in range(len(arr)):
        add+=arr[right]
        while add>k:
            add-=arr[left]
            left+=1
        max_len=max(max_len,right-left+1)
    return max_len
print(longest([2,3,1,4,2],6))  
'''
#Find the smallest sub-array with sum is greater than or equal to k?
# arr=[2,3,1,4,2]
# k=6
def smallest(arr,k):
    left=0
    right=0
    add=0
    min_len = float('inf')                     #min_len=len(arr)+1
    for right in range(len(arr)):
        add+=arr[right]
        while add>=k:
            min_len=min(min_len,right-left+1)
            add-=arr[left]
            left+=1
    return 0 if min_len==float('inf') else min_len
print(smallest([2,3,1,4,2],6))  
#leetcode:209,904,713