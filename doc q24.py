# Q24.
# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# print(a["item"])
# a=[[1,2,3],[4,5,6],[7,8,9]]



# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a[j]):
#             if i==k:
#                 print(a[j][k],end=" ")
#             k=k+1
#         j=j+1
#     print()
#     i=i+1

# a=[1,2,3]
# b=["priti","gaurav","nikita"]
# d={}
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)
#             print(j)
#             d.update({i:j})
# print(d)