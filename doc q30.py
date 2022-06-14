# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 
# 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
# a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 
# 'English']}
# a = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

# student_list = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

d = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
d1= {}
for i,j in d.items():
    for x in " ":
        i = i.replace(x,"")
        d1[i]= j
print(d1) 


a=["my name is monika?,i dont use","what happen"]
print(len(a))
print(len(a[0]))
print(len(a[1]))
for i in range(len(a)):
    k=""
    for j in range(len(a[i])):
        if a[i]==" ":
            
        j=j+1
    print(k)
    i=i+1