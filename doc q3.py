
# Q3.Write a Python script to generate and print a dictionary that contains a number
#  (between 1 and n) 

n=int(input("enter:"))
dic={}
i=1
while i<=n:
    print(i)
    dic.update({i:i*i})
    i=i+1
print(dic)

dic={}
n=int(input("enter:"))
for i in range(1,n+1):
    dic.update({i:i*i})
print(dic)
#     
