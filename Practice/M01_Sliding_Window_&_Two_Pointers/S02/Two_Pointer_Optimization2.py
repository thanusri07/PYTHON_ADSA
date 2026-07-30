'''remove the odd and print even num brom array'''

# b=list(map(int,input().split()))
# c=[ ]
# for i in range(len(b)):
#     if b[i]%2==0:
#         c.append(b[i])
# print(c)
'''optimised form using two pointers'''
# b=list(map(int,input().split()))
# left=0
# for right in range(len(b)):
#     if b[right]%2==0:
#         b[left]=b[right]
#         left+=1

# print(b[:left])


