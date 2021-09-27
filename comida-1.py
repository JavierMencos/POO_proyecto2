from pandas.core.algorithms import mode
from tabulate import tabulate
import soporte as spt
import pandas as pd

def desayuno():
    lista1 = []
    print('Escoja los alimentos que desea para desayunar.')
    print('Se deben comer 2 porciones de fruta, 1 porcion de lacteos, 1 embutido, huevo, 1 verdura, 2 porciones de cereales')
    comidas = [["COMIDAS","CANTIDAD"],
               ["Leche descremada", 'vaso mediano'],
               ["Leche descremada en polvo", "2 cdas en un vaso mediano"],
               ["Yogurt natural bajo en polvo","1 taza"],
               ["Leche entera","1 vaso mediano"],
               ["Leche entera en polvo","2 cdas en un vaso mediano"],
               ["Yogurt","1/2 taza"],
               ["Huevo","1 unidad"],
               ["Tomate","1/2 unidad"],
               ["Cebolla","1/4 de unidad"],
               ["Espinaca",'1/2 taza'],
               ["Chile pimientos","1/2 unidad"],
               ["Salchicha","1 unidad"],
               ["Jamon","1 rodaja"],
               ["Platano cocido","1/4 de unidad"],
               ["Frijol cocido","2 cucharadas"],
               ["Atol","1/2 taza"],
               ["Cereales de desayuno","3/4 de taza"],
               ["Banano","1 unidad"],
               ["Manzana","1/2 unidad"],
               ["Sandia","1 rodaja"],
               ["Papaya","1 rodaja"],
               ["Piña","1 rodaja"]]
    #indices, misma cantidad que los valores a mostrar, exceptuando loe encabezados
    indices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    print(tabulate(comidas, headers='firstrow', tablefmt='fancy_grid',showindex= indices))
    
    seleccion = spt.conversion_desayuno()
    #obetener comida y cantidad al dia de la lista principal.
    for i in range(len(seleccion)):
        for j in range(len(comidas)):
            if (seleccion[i]) == (j):
                lista1.append(comidas[j])

    #obtener la comida de manera mas limpia.
    comida1 = lista1[0][0]
    cantidad1 = lista1[0][1]

    comida2 = lista1[1][0]
    cantidad2 = lista1[1][1]

    comida3 = lista1[2][0]
    cantidad3 = lista1[2][1]
    
    comida4 = lista1[3][0]
    cantidad4 = lista1[3][1]
    
    comida5 = lista1[4][0]
    cantidad5 = lista1[4][1]
    
    comida6 = lista1[5][0]
    cantidad6 = lista1[5][1]
    
    comida7 = lista1[6][0]
    cantidad7 = lista1[6][1]
    
    comida8 = lista1[7][0]
    cantidad8 = lista1[7][1]
    
    with open("comidas.csv", mode="a+", encoding="utf-8") as df:
        #escritor = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #columnas = ['Comida', 'Cantidad']
        #escritor.writerow(columnas)
        guardar0 = df.write(f"Desayuno\n{comida1} , {cantidad1}\n")
        guardar1 = df.write(f"{comida2} , {cantidad2}\n")
        guardar2 = df.write(f"{comida3} , {cantidad3}\n")
        guardar3 = df.write(f"{comida4} , {cantidad4}\n")
        guardar4 = df.write(f"{comida5} , {cantidad5}\n")
        guardar5 = df.write(f"{comida6} , {cantidad6}\n")
        guardar6 = df.write(f"{comida7} , {cantidad7}\n")
        guardar7 = df.write(f"{comida8} , {cantidad8}\n")



def almuerzo():
    lista1 = []
    print('Escoja los alimentos que desea para almorzar.')
    print('Se debe comer al menos 4 onzas de carne, 2 cereales, 3 vereduras, 1 fruta y 1 grasa.')
    comidas = [["COMIDAS","CANTIDAD"],
               ["Carne de res","4 onzas"],
               ["Carne de cerdo","4 onzas"],
               ["Pescado","4 onzas"],
               ["Aceite","1 cucharada"],
               ["Aguacate","1/4 de unidad"],
               ["Tortilla","1 unidad"],
               ["Papa","2 unidades"],
               ["Pure de papa","1/2 taza"],
               ["Arvejas","1/2 taza"],
               ["Arroz cocido","1/2 taza"],
               ["Pasta","1/2 taza"],
               ["Elote","1 unidad mediana"],
               ["Garbanzos","1/2 taza cocida"],
               ["Lentejas","1/2 taza cocida"],
               ["Yuca","1/4 de taza"],
               ["Ejotes","1/2 taza cocida"],
               ["Remolacha","1/2 taza cocida"],
               ["Brocoli","1/2 taza"],
               ["Zanahoria","1/2 taza"],
               ["Pepino","1/2 taza"],
               ["Lechuga","Libre"],
               ["Rabano","Libre"],
               ["Berros","Libre"],
               ["Fresas","13 unidades"],
               ["Mandarinas","1 unidad"],
               ["Melon","1/4 de unidad"],
               ["Piña","1 rodaja"],
               ["Sandia","1 rodaja"],
               ["Pera","1/2 unidad"]]
    #indices, mismca cantidad que los valores a mostrar, exceptuando loe encabezados
    indices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    print(tabulate(comidas, headers='firstrow', tablefmt='fancy_grid',showindex= indices))

    seleccion = spt.conversion_almuerzo()
    #obetener comida y cantidad al dia de la lista principal.
    for i in range(len(seleccion)):
        for j in range(len(comidas)):
            if (seleccion[i]) == (j):
                lista1.append(comidas[j])

    #obtener la comida de manera mas limpia.
    comida1 = lista1[0][0]
    cantidad1 = lista1[0][1]

    comida2 = lista1[1][0]
    cantidad2 = lista1[1][1]

    comida3 = lista1[2][0]
    cantidad3 = lista1[2][1]
    
    comida4 = lista1[3][0]
    cantidad4 = lista1[3][1]
    
    comida5 = lista1[4][0]
    cantidad5 = lista1[4][1]
    
    comida6 = lista1[5][0]
    cantidad6 = lista1[5][1]
    
    comida7 = lista1[6][0]
    cantidad7 = lista1[6][1]
    
    comida8 = lista1[7][0]
    cantidad8 = lista1[7][1]
    
    with open("comidas.csv", mode="a+", encoding="utf-8") as df:
        #escritor = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #columnas = ['Comida', 'Cantidad']
        #escritor.writerow(columnas)
        guardar0 = df.write(f"Almuerzo\n{comida1} , {cantidad1}\n")
        guardar1 = df.write(f"{comida2} , {cantidad2}\n")
        guardar2 = df.write(f"{comida3} , {cantidad3}\n")
        guardar3 = df.write(f"{comida4} , {cantidad4}\n")
        guardar4 = df.write(f"{comida5} , {cantidad5}\n")
        guardar5 = df.write(f"{comida6} , {cantidad6}\n")
        guardar6 = df.write(f"{comida7} , {cantidad7}\n")
        guardar7 = df.write(f"{comida8} , {cantidad8}\n")

def merienda():
    lista1 = []
    print('Escoja los alimentos que desea para la merienda.')
    print('Se deben comer 3 cosas de la lista a continuacion.')
    comidas = [["COMIDAS","CANTIDAD"],
               ["Yogurt natural bajo en polvo","1 taza"],
               ["Yogurt","1/2 taza"],
               ["Banano","1 unidad"],
               ["Manzana","1/2 unidad"],
               ["Sandia","1 rodaja"],
               ["Papaya","1 rodaja"],
               ["Piña","1 rodaja"],
               ["Galletas dulces","4 unidades"],
               ["Crotones","1 taza"],
               ["Poporopos de maiz","3 tazas"],
               ["Jelatina","2 cucharadas"],
               ["Nueces","4 unidades"],
               ["Manias","8 unidades"],
               ["Almendras","6 unidades"]]
    #indices, misma cantidad que los valores a mostrar, exceptuando loe encabezados
    indices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print(tabulate(comidas, headers='firstrow', tablefmt='fancy_grid',showindex= indices))
    
    seleccion = spt.conversion_merienda()
    #obetener comida y cantidad al dia de la lista principal.
    for i in range(len(seleccion)):
        for j in range(len(comidas)):
            if (seleccion[i]) == (j):
                lista1.append(comidas[j])

    #obtener la comida de manera mas limpia.
    comida1 = lista1[0][0]
    cantidad1 = lista1[0][1]

    comida2 = lista1[1][0]
    cantidad2 = lista1[1][1]

    comida3 = lista1[2][0]
    cantidad3 = lista1[2][1]
     
    with open("comidas.csv", mode="a+", encoding="utf-8") as df:
        #escritor = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #columnas = ['Comida', 'Cantidad']
        #escritor.writerow(columnas)
        guardar0 = df.write(f"Merienda\n{comida1} , {cantidad1}\n")
        guardar1 = df.write(f"{comida2} , {cantidad2}\n")
        guardar2 = df.write(f"{comida3} , {cantidad3}\n")

def cena():
    lista1 = []
    print('Escoja los alimentos que desea para cenar.')
    print('Se deben comer 1 lacteo, 2 carnes, 1 cereal, 1 grasa, 3 verduras y 1 fruta.')
    comidas = [["COMIDAS","CANTIDAD"],
               ["Leche descremada", 'vaso mediano'],
               ["Leche descremada en polvo", "2 cdas en un vaso mediano"],
               ["Yogurt natural bajo en polvo","1 taza"],
               ["Leche entera","1 vaso mediano"],
               ["Leche entera en polvo","2 cdas en un vaso mediano"],
               ["Yogurt","1/2 taza"],
               ["Huevo","1 unidad"],
               ["Tomate","1/2 unidad"],
               ["Cebolla","1/4 de unidad"],
               ["Espinaca",'1/2 taza'],
               ["Chile pimientos","1/2 unidad"],
               ["Salchicha","1 unidad"],
               ["Jamon","1 rodaja"],
               ["Platano cocido","1/4 de unidad"],
               ["Frijol cocido","2 cucharadas"],
               ["Atol","1/2 taza"],
               ["Cereales de desayuno","3/4 de taza"],
               ["Banano","1 unidad"],
               ["Manzana","1/2 unidad"],
               ["Sandia","1 rodaja"],
               ["Papaya","1 rodaja"],
               ["Piña","1 rodaja"],
               ["Lechuga","Libre"],
               ["Brocoli","1/2 taza"],
               ["Zanahoria","1/2 taza"],
               ["Limon","4 unidades"],
               ["Pepino","1/2 taza"],
               ["Camote","1/3 de taza"],
               ["Mayonesa","1 cucharada"],
               ["Adoreso para ensalada","1 cucharada"],
               ["Atun en agua","1/4 de taza"],
               ["Requeson","2 cucharadas"],
               ["Queso cottage","1/4 de taza"],
               ["Sardinas","2 medianas"],
               ["Galletas saladas","6 unidades"]]
    
    #indices, misma cantidad que los valores a mostrar, exceptuando loe encabezados
    indices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    print(tabulate(comidas, headers='firstrow', tablefmt='fancy_grid',showindex= indices))
    
    seleccion = spt.conversion_cena()
    #obetener comida y cantidad al dia de la lista principal.
    for i in range(len(seleccion)):
        for j in range(len(comidas)):
            if (seleccion[i]) == (j):
                lista1.append(comidas[j])

    #obtener la comida de manera mas limpia.
    comida1 = lista1[0][0]
    cantidad1 = lista1[0][1]

    comida2 = lista1[1][0]
    cantidad2 = lista1[1][1]

    comida3 = lista1[2][0]
    cantidad3 = lista1[2][1]
    
    comida4 = lista1[3][0]
    cantidad4 = lista1[3][1]
    
    comida5 = lista1[4][0]
    cantidad5 = lista1[4][1]
    
    comida6 = lista1[5][0]
    cantidad6 = lista1[5][1]
    
    comida7 = lista1[6][0]
    cantidad7 = lista1[6][1]
    
    comida8 = lista1[7][0]
    cantidad8 = lista1[7][1]
    
    comida9 = lista1[8][0]
    cantidad9 = lista1[8][1]
        
    with open("comidas.csv", mode="a+", encoding="utf-8") as df:
        #escritor = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #columnas = ['Comida', 'Cantidad']
        #escritor.writerow(columnas)
        guardar0 = df.write(f"Cena\n{comida1} , {cantidad1}\n")
        guardar1 = df.write(f"{comida2} , {cantidad2}\n")
        guardar2 = df.write(f"{comida3} , {cantidad3}\n")
        guardar3 = df.write(f"{comida4} , {cantidad4}\n")
        guardar4 = df.write(f"{comida5} , {cantidad5}\n")
        guardar5 = df.write(f"{comida6} , {cantidad6}\n")
        guardar6 = df.write(f"{comida7} , {cantidad7}\n")
        guardar7 = df.write(f"{comida8} , {cantidad8}\n")
        guardar8 = df.write(f"{comida9} , {cantidad9}\n")

desayuno()
almuerzo()
merienda()
cena()