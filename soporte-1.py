
def conversion_desayuno():
    lista = []
    for i in range(8):
        repetir = True
        while repetir:
            try:
                comida = int(input("Ingrese la comida que desea, segun su indice (1,2,3...): "))
                if (comida <= 0) or (comida > 22):
                    print("DEBE INGRESAR UN VALOR SEGUN LOS INIDICES.")
                else:
                    lista.append(comida)
                    break
            except:
                print("DEBE INGRESAR UN VALOR NUMERIDO.")
                repetir = True
    return (lista)

def conversion_almuerzo():
    lista = []
    for i in range(8):
        repetir = True
        while repetir:
            try:
                comida = int(input("Ingrese la comida que desea, segun su indice (1,2,3...): "))
                if (comida <= 0) or (comida > 29):
                    print("DEBE INGRESAR UN VALOR SEGUN LOS INIDICES.")
                else:
                    lista.append(comida)
                    break
            except:
                print("DEBE INGRESAR UN VALOR NUMERIDO.")
                repetir = True
    return (lista)

def conversion_merienda():
    lista = []
    for i in range(3):
        repetir = True
        while repetir:
            try:
                comida = int(input("Ingrese la comida que desea, segun su indice (1,2,3...): "))
                if (comida <= 0) or (comida > 14):
                    print("DEBE INGRESAR UN VALOR SEGUN LOS INIDICES.")
                else:
                    lista.append(comida)
                    break
            except:
                print("DEBE INGRESAR UN VALOR NUMERIDO.")
                repetir = True
    return (lista)

def conversion_cena():
    lista = []
    for i in range(9):
        repetir = True
        while repetir:
            try:
                comida = int(input("Ingrese la comida que desea, segun su indice (1,2,3...): "))
                if (comida <= 0) or (comida > 35):
                    print("DEBE INGRESAR UN VALOR SEGUN LOS INIDICES.")
                else:
                    lista.append(comida)
                    break
            except:
                print("DEBE INGRESAR UN VALOR NUMERIDO.")
                repetir = True
    return (lista)