milena = (3,11,2004)
jose = (10,8,2005)

if milena [2] < jose [2]:
    print("milena é mais velha que jose")
elif jose[2] < milena[2]:
    print("jose é mais velho que milena")
elif jose [2] == milena [2]:
    if milena[1]> jose [1]:
        print("jose é mais velho que milena")
    elif jose [1] > milena [1]:
        print("jose e mais novo que milena")
    elif milena [1] == jose [1]:
        if milena [0] < jose [0]:
            print ("milena e mais velha que jose")
        elif jose [0] < milena[0]:
            print("jose e mais velho que milena")
    

