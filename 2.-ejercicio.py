
primera=input("Ingrese la Primera palabra: ")
primera=primera.replace(" ","")
primera=primera.lower()
segunda=input("Ingrese la Segunda palabra: ")
segunda=segunda.replace(" ","")
segunda=segunda.lower()
if primera==segunda:
    print("Ingrese dos palabras que sean distintas")
elif len(primera)< 3 and 3 > len(segunda):
    print("Ingrese palabras con más letras")
else:
    x1 = primera[-3:] 
    x2 = segunda[-3:]
    x3 = primera[-2:]
    x4 = segunda[-2:]
    rima1= primera[-1:-3]
    rima2= segunda[-1:-3]

    if x1 == x2:
        print("Las palabras riman")
    elif x3 == x4:
        print("Las palabras riman un poco")
    elif rima1 == rima2 :
        print("Las palabras riman")
    else:
        print("Las palabras no riman")