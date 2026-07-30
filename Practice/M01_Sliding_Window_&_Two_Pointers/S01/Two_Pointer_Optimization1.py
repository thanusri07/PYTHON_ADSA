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