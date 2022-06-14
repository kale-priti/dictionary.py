# a=['a',2,[],3,[],[],'c']
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])!=list:
#         b.append(a[i])
#         print(b)
#     i=i+1

# a={"apple":34,"boll":98}
# b={}
# k=()
# for i in a:
#     k.append({i:a[i]})
# print(k)

a=int(input("enter :"))
i=1 
b={}
while i<=a:
    b.update({i:print(i%2==0)})
    i=i+1
print(b)
