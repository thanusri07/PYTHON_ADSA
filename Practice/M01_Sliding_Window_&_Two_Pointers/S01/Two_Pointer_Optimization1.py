''' Two pointers uses 2 Variables and can print from two sides which reduces time and space complexities used in 
* Arrays
*Lists
*Strings
*Linkedlist
*slinding windows
'''
'''O(n^2)'''
# b=list(map(int,input().split()))
# T=5
# found=False
# for i in range(len(b)):
#     for j in range(i+1,len(b)):
#         if b[i]+b[j]==T:
#             found=True
#             print(i,j)
#             break
#     if found:
#         break
# if not found:
#     print("Not found")
'''O(n)'''
# b=list(map(int,input().split()))
# T=5
# found=False
# Left,Right=0,len(b)-1
# while Left<Right:
#     add=b[Left]+b[Right]
#     if add==T:
#         found=True
#         print(Left,Right)
#         break
#     elif add<T:
#         Left+=1
#     else:
#         Right-=1
# if not found:
#     print("No pairs found")

'''Reversing a String'''#without slicing
'''Treditional approach'''
''' first use list to convert into list and use join in print so it is print in the form of string'''
# s="hello"
# rev=" "
# for ch in s:
#     rev=ch+rev
# print(rev)

# s = "hello"
# ch = list(s)

# left,right = 0,len(ch) - 1

# while left < right:
#     ch[left], ch[right] = ch[right], ch[left]
#     left += 1
#     right -= 1

# print("".join(ch))
'''Two Pointers:
Definition: Two pointers is a technique that uses two pointers to iterate through a data structure, 
such as an array or a linked list, to solve problems efficiently. 
Types:
1. opposite direction: In this type, two pointers are initialized at the beginning and end of the data structure,Opposite direction 
2. same direction: In this type, two pointers are initialized at the same position and move in the same direction through the data structure.

Two Sum :

arr=[2,3,4,5,6]
target=11
found =False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            found=True
            print("Pair found at index",i,"and",j)
            break
    if found:
        break
if not found:
    print("Pair not found")
'''
arr=[2,3,4,5,6]
target=11
found =False
left,right=0,len(arr)-1
while left<right:
    if arr[left]+arr[right]==target:
        found=True
        print("Pair found at index",left,"and",right)
        break
    elif arr[left]+arr[right]<target:
        left+=1
    else:
        right-=1
if not found:
    print("Pair not found")