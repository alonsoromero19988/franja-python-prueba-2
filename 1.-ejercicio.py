def palabra_larga(Plbra):
    largo=[]
    for i in Plbra:
        largo.append((len(i),i))

        largo.sort()
    return largo[-1][1]    

def main ():
    plbra= ['cazadores','munmicipalidad','inadaptados','trancado']
    print(palabra_larga(plbra))

main ()
