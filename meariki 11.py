# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100,
#     'f':20
# }
# # print(max(my_dict,key=my_dict.get))
# max=0
# sec_max=0
# thrid_max=0
# for i in my_dict:
#     for j in my_dict:
#         if my_dict[j]>=max:
#             max=my_dict[j]
#         if my_dict[j]>sec_max and my_dict[j]!=max:
#             sec_max=my_dict[j]
#         if my_dict[j]>thrid_max and my_dict[j]!=max and my_dict[j]!=sec_max:
#             thrid_max=my_dict[j]
# print(max)
# print(sec_max)
# print(thrid_max)




my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100,
    'f':20
}
# print(max(my_dict,key=my_dict.get))
max=0
b=[]
sec_max=0
thrid_max=0
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>=max:
            max=my_dict[j]
            max_1=j
        if my_dict[j]>sec_max and my_dict[j]!=max:
            sec_max=my_dict[j]
            max_2=j
        if my_dict[j]>thrid_max and my_dict[j]!=max and my_dict[j]!=sec_max:
            thrid_max=my_dict[j]
            max_3=j
# print(max)
# print(sec_max)
# print(thrid_max)
# print(max_1)
# print(max_2)
# print(max_3)
b.append(max_1)
b.append(max_2)
b.append(max_3)
print(b)