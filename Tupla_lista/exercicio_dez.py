tupla1 = ("espirito santo", "rio grande do sul", "rio de janeiro", "sao paulo", "minas gerais ")
tupla2 = ()

for t in tupla1:
    tupla2 += (len(t), )

print (tupla2)    