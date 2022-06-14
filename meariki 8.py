# {
#  'sonu':85,
#  'Kartik':90,
#  'Deepak':96,
#  'Aman':76,
#  'Somesh':60,
#  'Umesh':85,
#  'Amarpal':70,
#  'Roshan':57,
#  'Riyaz':98,
#  'Shabid':56
# }
a=int(input("enter the len"))
s={}
i=0
while i<a:
    b=input("enter the key name")
    k=int(input("enter the num"))
    s.update({b:k})
    i=i+1
print(s)