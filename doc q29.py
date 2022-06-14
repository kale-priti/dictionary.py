# Q29.Write a Python program to sort a list alphabetically in a dictionary.
l=["r","t","e","h"]
z={}
for i in  range (len(l)):
    for j in range (len(l)):
        if l[i]>l[j]:
            z.update({l[i]:l[j]})
print(z)

