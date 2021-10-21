# Encabezado
import random

def menu_principal():

    # Este es el menu principal del proyecto:

    # Raxnaquil2

    print("\n--------------- Menu principal de Raxnaquil 2 ---------------\n")
    print("[ 1 ] Ingresar usuario")
    print("[ 2 ] Registrar usuario")
    print("")

    respuesta = input("Opcion: ")

    while(True):

        if respuesta == "1" or respuesta == "2":

            return respuesta

        else:

            print(" ! Opcion no reconocida, porfavor intente de nuevo...")

            respuesta = input("Opcion: ")

def pedir_datos_loggeo():
    print("\n--------------- Menu de loggeo de Raxnaquil 2---------------\n")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    return [usuario,clave]

def paciente_encontrado_doctor(nombrepaciente, nombredoctor , carnetdoctor , ubi, precio):
    print("")
    print("Departamento: " + str(ubi.split("-")[1]).upper() + " | " + "Zona: " + str(ubi.split("-")[0]))
    print("\nPerfecto " + nombrepaciente + ", hemos encontrado al doctor " + nombredoctor + " que te antendera con gusto.")
    print("Porfavor refierete a el en el hospital con su numero de carnet: " + carnetdoctor + " | Precio por consulta: " + precio + "$\n")
    pass

def elegir_sintoma_usuario():

    print("\nPorfavor diganos su sintoma actual:\n")
    lista_sintomas = ["Cabeza","Cuello","Pecho","Dorso","Espalda","Cintura","Pierna","Brazo","Pie","Mano","Otros"]
    for i in range(len(lista_sintomas)):
        print( "[ " +str(i + 1) + " ] " + lista_sintomas[i])
    print("")
    respuesta = ""
    while(True):
        respuesta = input("Sintoma: ").capitalize()
        if respuesta in lista_sintomas:
            return respuesta
        else:
            print(" ! Opcion no reconocida, porfavor intente de nuevo...")

def elegir_presupuesto_usuario():

    print("\nPorfavor diganos su presupuesto actual:\n")
    lista_costos = ["20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55",
                    "56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91",
                    "92","93","94","95","96","97","98","99","100"]
    for i in range(len(lista_costos)):
        print( "[ " +str(i + 1) + " ] " + lista_costos[i])
    print("")
    respuesta = ""
    while(True):
        respuesta = input("Presupuesto: ").capitalize()
        if respuesta in lista_costos:
            return respuesta
        else:
            print(" ! Opcion no reconocida, actualmemte no hay doctores con precios tan altos o tan bajos, porfavor intente de nuevo...")

def dejar_calificacion():

    print("\n--------------- Menu de calificacion de Raxnaquil 2---------------\n")

    print("Para comenzar, porfavor ingrese el carnet del doctor al que desea calificar:")

    carnet_doctor = input("Carnet: ")

    doctor_econtrado = False

    doctor = {}
    apellido = ""
    carnet   = ""
    f = open("datosDoctores.csv", "r")
    for doc in f.readlines():
        dnd = doc.replace("\n","").split(",")
        # (nombre_usuario) (clave) Nombre - Apellido - Carnet - Precio Cobra / consulta - Especialidad - Ubicacion
        if carnet_doctor == dnd[5]:
            doctor[dnd[4]] = dnd[3]
            apellido = dnd[3]
            carnet = dnd[5]
            doctor_econtrado = True
        #for doc in f.readlines():
             #print("Usuario encontrado")
             #dnd = doc.replace("\n","").split(",")
             #D = Doctor(dnd[0],dnd[1],dnd[2],dnd[3],dnd[4],dnd[5],dnd[6],dnd[7])
             #lista_doctores_temp.append(D)
    
    if doctor_econtrado:

        print("\nPorfavor deje su calificacion y comentarios para el Dr." + apellido + ":")

        comentario = input("Comentario: ").replace(",","")

        # with open("relacionesdoctor.csv","a") as archivo:
        #     archivo.write(str(doctor.nombre_usuario) + "," + str(paciente.nombre_usuario) + "\n")

        with open("calificaciones.csv","a") as archivo:
            archivo.write(carnet_doctor + "," + comentario + "\n")

        pass

    else:

        print("\n ! El doctor no ha sido encontrado, porfavor intenta de nuevo..\n")

    pass

def elegir_especialidad_doctor():

    print("\nPorfavor diganos su especialidad:\n")
    lista_sintomas = ["Cabeza","Cuello","Pecho","Dorso","Espalda","Cintura","Pierna","Brazo","Pie","Mano","Otros"]
    for i in range(len(lista_sintomas)):
        print( "[ " +str(i + 1) + " ] " + lista_sintomas[i])
    print("")
    respuesta = ""
    while(True):
        respuesta = input("Especialidad: ").capitalize()
        if respuesta in lista_sintomas:
            return respuesta
        else:
            print(" ! Opcion no reconocida, porfavor intente de nuevo...")


def generar_olla_alimenticia_usuario(paciente):

    print("\n--------------- Menu de olla alimenticia de Raxnaquil ---------------\n")

    lista_generos = ["Hombre","Mujer"]

    genero = ""

    while(True):

        genero = input("Porfavor elija un genero [ Hombre / Mujer ]: ")
        if genero in lista_generos:
            break
        else:
            print(" ! Genero no reconocido, porfavor intente de nuevo...")

    presupuesto = 0

    while(True):

        try:
            presupuesto = int(input("Porfavor ingrese su presupuesto: "))
            if presupuesto < 200:
                # No puede ser tan bajo:
                print(" ! El presupuesto tiene que ser un numero mayor a 200Q, porfavor intente de nuevo...")
                pass
            else:
                break
        except:
            print(" ! El presupuesto tiene que ser un numero entero, porfavor intente de nuevo...")
            pass

    # para 300Q 
    # Carne a la semana 2 veces    1kg carne 70Q
    # Lacteos 3 veces a la semana   30Q
    # Carbohidratos y cereales 21 veces   10Q
    # Frutas y verduras 7 veces   =6Q + 3Q 

    presupuesto_para_carnes = (presupuesto / 8)
    presupuesto_para_lacteos = (presupuesto / 8)
    presupuesto_para_cereales = (presupuesto / 8) * 4
    presupuesto_para_verfruts = (presupuesto / 8) * 2

    peso_usuario = int(paciente.peso_paciente)
    esta_usuario = paciente.estatura_paciente

    diccionario_relacion_peso_altura_hombres = {1.57:58.1,
                                                1.58:54.8}
    diccionario_relacion_peso_altura_mujeres = {1.57:53.7,
                                                1.58:54.3}

    if genero == "Hombre":

        #Comparar la estatura con el peso: Si es mayo es sobre peso
        # print(esta_usuario)
        # print(diccionario_relacion_peso_altura_hombres[float(esta_usuario)])
        # print(peso_usuario)
        if peso_usuario > diccionario_relacion_peso_altura_hombres[float(este_usuario)]:

            # Tiene sobrepeso haga ejercicio:

            print("\nSe le recomienda hacer ejercicio para bajar un poco su peso. Visite la siguiente pagina para tener una guia de como hacerlo:")
            print("URL")
    
        else:

            # Si cumple con el peso indicado, ponerle su dieta:

            lista_carnes = [["Res",13],["Pollo",12],["Cerdo",10]] # La suma de dos precios no puede ser mayor a 25
            lista_lactes = [["Leche",10],["Queso",10],["Yougurt",5]]
            lista_carboh = [["Arroz",4],["Maiz",4.5],["Frijol",4]] # No se puede pasar de 4.75
            lista_verfru = [["Banano",3],["Aguacate",4],["Sandia",7]] # No se puede pasar de 7Q

            print("Imprimiendo olla alimenticia de esta semana de acorde a su presupuesto:")
            print("Listando sus 2 porciones de carnes a la semana:")
            for i in range(2):
                carne_electa = lista_carnes[random.randint(0,len(lista_carnes) - 1)]
                print(str(i + 1) + " " + carne_electa[0] + " Precio: " + str(carne_electa[1]))
            print("Listando sus 3 porciones de lacteos a la semana:")
            for i in range(3):
                lacteo_electo = lista_lactes[random.randint(0,len(lista_lactes)- 1)]
                print(str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
            print("Listando sus 21 porciones de carbohidratos a la semana:")
            diccionario_carbo = {}
            for i in range(len(lista_carboh)):
                diccionario_carbo[lista_carboh[i][0]] = 0
            for i in range(21):
                carboh_electo = lista_carboh[random.randint(0,len(lista_carboh)- 1)]
                diccionario_carbo[carboh_electo[0]] = diccionario_carbo[carboh_electo[0]] + 1
                # print(str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
            print(diccionario_carbo)
            print("Listando sus 7 porciones de frutas y verduras a la semana:")
            for i in range(7):
                frutaver_electa = lista_verfru[random.randint(0,len(lista_verfru)- 1)]
                print(str(i + 1) + " " + frutaver_electa[0] + " Precio: " + str(frutaver_electa[1]))
    if genero == "Mujer":

        #Comparar la estatura con el peso: Si es mayo es sobre peso
        if peso_usuario > diccionario_relacion_peso_altura_mujeres[float(esta_usuario)]:

            # Tiene sobre peso haga ejercicio:

            print("\nSe le recomienda hacer ejercicio para bajar un poco su peso. Visite la siguiente pagina para tener una guia de como hacerlo:")
            print("URL")

        else:
            # Si cumple con el peso indicado, ponerle su dieta:

            lista_carnes = [["Res",13],["Pollo",12],["Cerdo",10]] # La suma de dos precios no puede ser mayor a 25
            lista_lactes = [["Leche",10],["Queso",10],["Yougurt",5]]
            lista_carboh = [["Arroz",4],["Maiz",4.5],["Frijol",4]] # No se puede pasar de 4.75
            lista_verfru = [["Banano",3],["Aguacate",4],["Sandia",7]] # No se puede pasar de 7Q

            print("Imprimiendo olla alimenticia de esta semana de acorde a su presupuesto:")
            print("Listando sus 2 porciones de carnes a la semana:")
            for i in range(2):
                carne_electa = lista_carnes[random.randint(0,len(lista_carnes)- 1)]
                print(str(i + 1) + " " + carne_electa[0] + " Precio: " + str(carne_electa[1]))
            print("Listando sus 3 porciones de lacteos a la semana:")
            for i in range(3):
                lacteo_electo = lista_lactes[random.randint(0,len(lista_lactes)- 1)]
                print(str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
            print("Listando sus 21 porciones de carbohidratos a la semana:")
            diccionario_carbo = {}
            for i in range(len(lista_carboh)):
                diccionario_carbo[lista_carboh[i][0]] = 0
            for i in range(21):
                carboh_electo = lista_carboh[random.randint(0,len(lista_carboh)- 1)]
                diccionario_carbo[carboh_electo[0]] = diccionario_carbo[carboh_electo[0]] + 1
                # print(str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
            print(diccionario_carbo)
            print("Listando sus 7 porciones de frutas y verduras a la semana:")
            for i in range(7):
                frutaver_electa = lista_verfru[random.randint(0,len(lista_verfru)- 1)]
                print(str(i + 1) + " " + frutaver_electa[0] + " Precio: " + str(frutaver_electa[1]))
            # Si cumple con el peso indicado, ponerle su dieta:


    

def menu_loggeo_paciente():
    print("\n--------------- Menu de paciente de Raxnaquil ---------------\n")
    # Modificar su area de dolor
    # Buscar un doctor
    # Modificar presupuesto
    # Calificar doctor
    # Cerrar sesion
    print("[ 1 ] Modificar sintoma")
    print("[ 2 ] Buscar doctor")
    print("[ 3 ] Modificar mi presupuesto")
    print("[ 4 ] Calificar a un doctor")
    print("[ 5 ] Generador de olla alimenticia")
    print("[ 6 ] Cerrar mi sesion\n")
    
    respuesta = input("Opcion: ")

    while(True):

        if respuesta in ["1","2","3","4","5"]:

            return respuesta

        else:

            print(" ! Opcion no reconocida, porfavor intente de nuevo...")

            respuesta = input("Opcion: ")

def menu_loggeo_doctor():
    print("\n--------------- Menu de doctor de Raxnaquil ---------------\n")
    # Ver que usuarios ha atendido
    # Ver sus calificaciones
    print("[ 1 ] observar reseñas")
    print("[ 2 ] mirar pacientes\n")
    
    respuesta = input("Opcion: ")
    
    while(True):
        
        if respuesta in ["1","2"]:
            
            return respuesta
        
        else:
            
            print(" ! Opcion no reconocida, porfavor intente de nuevo...")
            
            respuesta = input("Opcion: ")

def recaudar_datos_doctor(numero):

    print("\n--------------- Menu de registro de Doctor de Raxnaquil ---------------\n")

    # (nombre_usuario) (clave) Nombre - Apellido - Carnet - Precio Cobra / consulta - Especialidad - Ubicacion

    print("Porfavor ingrese su nombre:")
    nombre = input("Nombre: ")
    print("Porfavor ingrese su apellido:")
    apellido = input("Apellido:")

    nombre_usuario = nombre[0] + apellido[0] + numero

    print("\nSu nombre de usuario sera: " + nombre_usuario + "\n")

    print("Porfavor ingrese su clave:")
    clave = input("Clave: ")

    print("Porfavor ingrese su carnet de doctor:")
    # Limitamos sus digitos
    carnet = ""
    while(True):
        carnet = input("Carnet: ")
        if len(carnet) > 6 or len(carnet) < 1:
            # Error
            print(" ! Carnet invalido, utilice entre 1 y 6 caracteres...")
        else:
            break

    print("Porfavor ingrese su precio por consulta:")
    precio = input("Precio: ")

    especialidad = elegir_especialidad_doctor()

    print("Porfavor ingrese la zona en la que se ubica:")
    zona = input("Zona: ")
    print("Porfavor ingrese su departamento: ")
    departamento = input("Departamento: ").lower()

    ubicacion = zona + "-" + departamento

    # (self, nombre_usuario, clave, nombre, apellido, ubicacion, carnet, precio , especialidad):
    return [nombre_usuario,clave,nombre,apellido,ubicacion,carnet,precio,especialidad]

def avisar_nuevo_sintoma(s):
    print("\nSu sintoma ha sido actualizado correctamente a " + s + "\n")

def avisar_nuevo_presupuesto(n):
    print("\nSu presupuesto ha sido actualizado correctamente a " + n + "\n")

def recaudar_datos_paciente(numero):

    print("\n--------------- Menu de registro de Paciente de Raxnaquil ---------------\n")

    # (nombre_usuario) (clave) Nombre - Apellido - Edad - Presupuesto - Estatura - Peso (Kg) - Sintomas - Ubicacion

    # Edad - Presupuesto - Estatura - Peso (Kg) - Sintomas

    print("Porfavor ingrese su nombre:")
    nombre = input("Nombre: ")
    print("Porfavor ingrese su apellido:")
    apellido = input("Apellido:")

    nombre_usuario = nombre[0] + apellido[0] + numero

    print("\nSu nombre de usuario sera: " + nombre_usuario + "\n")

    print("Porfavor ingrese su clave:")
    clave = input("Clave: ")

    print("Porfavor ingrese su edad:")
    edad = input("Edad: ")

    print("Porfavor ingrese su presupuesto:")
    presupuesto = input("Presupuesto: ")

    print("Porfavor ingrese su estatura:")
    estatura = input("Estatura: ")

    print("Porfavor ingrese su peso en KG: ")
    peso = input("Peso: ")

    sintoma = elegir_sintoma_usuario()

    print("Porfavor ingrese la zona en la que vive:")
    zona = input("Zona: ")
    print("Porfavor ingrese su departamento: ")
    departamento = input("Departamento: ").lower()

    ubicacion = zona + "-" + departamento

    # (nombre_usuario) (clave) Nombre - Apellido - Edad - Presupuesto - Estatura - Peso (Kg) - Sintomas - Ubicacion

    # (self, nombre_usuario, clave, nombre, apellido, ubicacion, edad, presupuesto, estatura, peso, sintoma):
    return [nombre_usuario,clave,nombre,apellido,ubicacion,edad,presupuesto,estatura,peso,sintoma]

def preguntar_tipo_usuario():

    # Este metodo sirve para ubicar que tipo de usuario sera registrado:

    print("\n--------------- Menu de registro de Raxnaquil 2---------------\n")

    print("[ 1 ] Registrar nuevo doctor")
    print("[ 2 ] Registrar nuevo paciente")
    print("")

    respuesta = input("Opcion: ")

    while(True):

        if respuesta == "1" or respuesta == "2":

            return respuesta

        else:

            print(" ! Opcion no reconocida, porfavor intente de nuevo...")

            respuesta = input("Opcion: ")
