# Q39.Write a Python program to filter a dictionary based on values. 
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox


d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165,'Pierre Cox': 190}
d2= {}
for i,j in d1.items():
    if j > 170:
        d2[i] = j
print(d2)