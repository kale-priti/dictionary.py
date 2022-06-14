# Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
#                 'P 0 3 ': 'Soft Computing'}

# d={}
# for i,j in Product_list.items():
#     print(i)
#     # print("s",j)

#     for x in " ":
#         i=i.replace(x,"")
#         print(i)
#         d[i]=j
# print(d)
# a={"priti":34,"gaurav":97,"lakhan":66}
# print(a["gaurav"]),a(["lakhan"])



a=[1,2,3]
b=["priti","gaurav","kale"]
d={}
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         if i==j:
#             d.update({a[i]:b[j]})
#         j=j+1
#     i=i+1
# print(d)


for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            d.update({a[i]:b[j]})
print(d)
