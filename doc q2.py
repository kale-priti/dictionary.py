
# Q2. Write a Python program to create a dictionary from a string.
a="w3resource"
# i=0
# d={}
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     d.update({a[i]:c})
#     i=i+1
# print(d)
d={}
for i in a:
    c=0
    for j in a:
        if i==j:
            c=c+1
    d.update({i:c})
print(d)
