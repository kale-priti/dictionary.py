# Q11.Write a Python script to merge two Python dictionaries
# a=int(input("enter the lenth:"))
# k={}
# for i  in range (1,a+1):
#     key_name=input("enter the key:")
#     key_value=input("enter the value:")
#     k.update({key_name:key_value})
# print(k)
# a=int(input("enter the lenth:"))
# dic={}
# for i  in range (1,a+1):
#     key_name=input("enter the key:")
#     key_value=input("enter the value:")
#     dic.update({key_name:key_value})
# print(dic)

a={"priti":87,"kale":97,"kachru":986}
b={"true":983,"gaurav":9863}
a.update(b)
print(a)
