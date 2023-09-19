tupla1 = (1,2,3,4,5,6,7,8,9)
tupla2 = ()
for t in tupla1:
    if t %2 == 0:
        tupla2 += (t, )

print (tupla2)


