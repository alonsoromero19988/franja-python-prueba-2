def areac(radio):
    area_circulo = 3.14*radio**2
    return area_circulo


def volumen(radio, altura):
    volumen_cilindro = areac(radio)*altura
    return volumen_cilindro

def main():
    print(areac(15))
    print(print(15,5))

if __name__ == '__main__':    
   main()