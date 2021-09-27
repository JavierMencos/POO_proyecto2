from tabulate import tabulate

def principal():
    print(" 1. Dieta de 1800 kcal\n",
          "2. Dieta general basica\n",
          "3. Valores nutricionales de los alimentos")
    opcion = validacion()
    if opcion == 1:
        dieta_1()
    if opcion == 2:
        dieta_2()
    if opcion ==3:
        nutricional()
    
def validacion():
    while True:
        try:
            opcion = int(input("Seleccione una de las opciones: "))
            if (opcion <= 0) or (opcion > 3):
                print("DEBE INGRESAR UN VALOR SEGUN EL MENU")
            else:
                break
        except:
            print("DEBE INGRESAR UN VALOR NUMERICO")
    return (opcion)            
    
def dieta_1():
    dieta1_desayuno = [['Desayuno', 'Desayuno'],
                       ["COMIDAS","CANTIDAD"],
                       ["Leche desnatada",'1 taza = 250g'],
                       ['Azucar','1 cucharada = 7g'],
                       ['Pan integral','2 rebanadas = 60g'],
                       ['Mermelada baja en calorias','1 cucharada = 13g'],
                       ['Zumo de naranja','1 vaso = 200g']]
    
    dieta1_almuerzo = [['Almuerzo', 'Almuerzo'],
                       ["COMIDAS","CANTIDAD"],
                       ['Arroz con verduras', '1 racion mediana'],
                       ['Pescadilla cocida','1 racion mediana'],
                       ['Pan integral','1 rebanada = 30g'],
                       ['Pera','1 unidad = 200g'],
                       ['Aceite de oliva','1 cucharada = 10g'],
                       ['Agua pura','1 vaso']]

    dieta1_merienda = [["Merienda", 'Merienda'],
                       ["COMIDAS","CANTIDAD"],
                       ["Cafe con leche entera y azucar", '1 taza y 1 cucharada = 160g'],
                       ['Pan integral','2 rebanadas = 60g'],
                       ['Manzana','1 unidad = 200g']]
    
    dieta1_cena = [["Cena", 'Cena'],
                   ["COMIDAS","CANTIDAD"],
                   ["Tortilla francesa de 1 huevo", '1 unidad'],
                   ['Carne de res','2 onza = 125g'],
                   ['Pan blanco','1 rebanda = 30g'],
                   ['Yogur desnatado','1 unidad = 125g'],
                   ['Aceite de oliva','1 cucharada = 10g'],
                   ['Agua pura','1 vaso']]

    print(tabulate(dieta1_desayuno, headers='firstrow', tablefmt='fancy_grid'))
    print(tabulate(dieta1_almuerzo, headers='firstrow', tablefmt='fancy_grid'))
    print(tabulate(dieta1_merienda, headers='firstrow', tablefmt='fancy_grid'))
    print(tabulate(dieta1_cena, headers='firstrow', tablefmt='fancy_grid'))

def dieta_2():
    dieta2_general = [['Grupos de alimentos','Raciones/dia','Peso de la racion'],
                      ['','','Leche = 200ml'],
                      ['Lacteos','','Yogur = 125g'],
                      ['(Usar descremados)','2 - 3','Queso fresco = 30g - 40g'],
                      ['','','Otros quesos = 15g - 20g'],
                      ['Grupos de alimentos','Raciones/dia','Peso de la racion'],
                      ['Carnes','','Carnes = 100g - 125g'],
                      ['Pescado','2','Pescados = 125g - 150g'],
                      ['Huevos','','Huevos = 1 unidad'],
                      ['Grupos de alimentos','Raciones/dia','Peso de la racion'],
                      ['','','Pan = 30g - 40g'],
                      ['','','Cereales desayuno = 30g - 40g'],
                      ['Cereales y legumbres','6','Arroz = 60g - 70g'],
                      ['','','Pasta = 60g - 70g'],
                      ['','','Legumbres = 60g - 70g'],
                      ['Grupos de alimentos','Raciones/dia','Peso de la racion'],
                      ['Frutas','3','Pieza mediana = 150g - 200g'],
                      ['','','1 vaso de zuma = 150ml'],
                      ['Grupos de alimentos','Raciones/dia','Peso de la racion'],
                      ['Verduras y hortalizas','3 - 4','100g - 200g']]
    
    dieta2_general2 = [['Grupos de alimentos','Raciones/dia'],
                       ['Aceites y grasas','Con moderacion'],
                       ['Azucares y dulces','Con moderacion'],
                       ['Bebidas no alcoholicas','Beber preferentemente agua'],
                       ['Bebidas alcoholicas','Con moderacion']]

    print(tabulate(dieta2_general, headers='firstrow', tablefmt='fancy_grid'))
    print(tabulate(dieta2_general2, headers='firstrow', tablefmt='fancy_grid'))

def nutricional():
    nutri = [['Nombre','Energia','Proteina','Carbohidratos','Grasa'],
             ['Incaparina','70kcal','7g','11g','0g'],
             ['Leches','135kcal','7g','11g','7g'],
             ['Vegetales','30kcal','0g','7g','0g'],
             ['Frutas','40kcal','0g','10g','0g'],
             ['Cereales','75kcal','3g','16g','0g'],
             ['Carnes','65kcal','7g','0g','4g'],
             ['Grasas','45kcal','0g','0g','5g'],
             ['Azucares','20kcal','0g','5g','0g']]
    
    print(tabulate(nutri, headers='firstrow', tablefmt='fancy_grid'))
