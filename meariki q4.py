  ### example ##

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

 ### example ##
# details={
# 'Name': 'RAM',
# 'Age': 17, 
# 'student': {
# 'id': 22,
# 'place': 'dharamsala'
# }
# } 
# details['student']['id']=35
# print(details);


#### use copy method ##
classes ={
"room1":  "6th",
"room2":  "7th",
"room3":  "8th"
}
mydict=classes.copy()
print(mydict)
# dict1={“name”:”Raju”, “marks”:56}
dict1={"name":"raju","mark":56}
a=input("enter the key")
if a in dict1:
    print("exist")
else:
    print("not exist")