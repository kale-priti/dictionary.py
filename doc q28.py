# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# a= [1, 2, 3, 4]
# d={}
# i=0
# while  i <len(a):
#     d={a[-i]:d}
#     i=i+1
# print(d)
    

a= [1, 2, 3, 4]
# n=d={}
d={}
# i=0
# while  i <len(a):
#     d={a[-i]:d}
#     i=i+1
# print(d)
    
for i in a:
    # print(-i)
    d={a[-i]:d}
print(d)

# for i in a:
#     d[i]={}
#     d=d[i]
# print(n)
