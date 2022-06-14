# a=[1,2,1,4,6,3,7,1,8,4,7,]
# a={"priti":34,"gaurav":866,"lakhan":{"riti":981,"riya":987}}
# print(len(a))
# print(a["lakhan"]["riya"])

# a=[1,3,1,2,4,5,1,3,2,4,5]
# a=[1,2,3,4,5,1,1,2,2,3]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

# dict1={}
# i=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     dict1.update({a[i]:c})
#     i=i+1
# print(dict1)


# a=int(input('enter the num:'))
# d={}
# for i in range(1,a+1):
#     if i%2==0:
#         d.update({i:True})
#     else:
#         d.update({i:False})
# print(d)

# a={1:{9:'p',3:'4'}}
# print(a[1][3])


# a={"p":[1,2,3],"k":[5,6,7]}
# b={}
# for i in a:
#     # print(a[i])
#     sum=0
#     for j in range (len(a[i])):
#         sum=sum+a[i][j]
#     b.update({i:sum})
# print(b)
    

# a=int(input("enter:"))
# b=a%2==0
# print("even")
# b=a%2!=0 print("odd")

a=[2,3,5,5]
max=0
sec_max=0
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>max:
            max=a[j]
        if a[j]>sec_max and a[j]!=max:
            sec_max=a[j]
        j=j+1
    i=i+1
print(sec_max)