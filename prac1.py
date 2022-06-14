# a={"priti":[12,42,23],"richa":[53,85,24]}
# b=[]
# for i in a:
#     for j in a[i]:
#         b.append(j)
# print(b)

a=["my name is priti?","how are you"]
# print(len(a))
# print(len(a[0]))
# print(len(a[1]))
n=[]
i=0
while i<len(a):
    b=a[i].replace(" ", "")
    print(b)
    n.append(len(b))
    i=i+1
print(n)

a=13
def sum():
    b=2
    c=a+b
    return c
v=sum()
print(v)
def summ():
    a=v+1
    print(a)
summ()





