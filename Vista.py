# Encabezo
import random

def menu_principal():

    # Este es el menu principal del proyecto:

    # Raxnaquil

    print("\n--------------- Menu principal de Raxnaquil ---------------\n")
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
    print("\n--------------- Menu de loggeo de Raxnaquil ---------------\n")
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

    presu = int(input("\nPorfavor diganos su presupuesto actual:\n"))
    
    while(True):
        respuesta = input("Presupuesto: ").capitalize()
        if (presu > 0):
            return respuesta
        else:
            print(" Opción incorrecta")

def dejar_calificacion():

    print("\n--------------- Menu de calificacion de Raxnaquil ---------------\n")

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

    diccionario_relacion_peso_altura_hombres = {1.5:50,
                                                1.51:50.5,
                                                1.52:51,
                                                1.53:54.4,
                                                1.54:52.1,
                                                1.55:52.6,
                                                1.56:53.2,
                                                1.57:58.1,
                                                1.58:54.8,
                                                1.59:59.6,
                                                1.6:60.3,
                                                1.61:60.9,
                                                1.62:61.4,
                                                1.63:61.8,
                                                1.64:62.5,
                                                1.65:63,
                                                1.66:63.7,
                                                1.67:64.4,
                                                1.68:65.1,
                                                1.69:65.6,
                                                1.7:66.6,
                                                1.71:67.4,
                                                1.72:68.3,
                                                1.73:69.1,
                                                1.74:69.8,
                                                1.75:70.8,
                                                1.76:71.3,
                                                1.77:72,
                                                1.78:72.8
                                                1.79:73.8,
                                                1.8:74.4,
                                                1.81:75.4,
                                                1.82:76.3,
                                                1.83:77.2,
                                                1.84:78.1,
                                                1.85:79,
                                                1.86:79.7,
                                                1.87:80.8,
                                                1.88:81.7,
                                                1.89:82.6,
                                                1.9:83.5,
                                                1.91:84.4,
                                                1.92:85.3,
                                                1.93:86}
    
    diccionario_relacion_peso_altura_mujeres = {1.5:50,
                                                1.51:50.5,
                                                1.52:51,
                                                1.53:54.4,
                                                1.54:52.1,
                                                1.55:52.6,
                                                1.56:53.2,
                                                1.57:53.7,
                                                1.58:54.3,
                                                1.59:54.8,
                                                1.6:55.3,
                                                1.61:59.4,
                                                1.62:56.6,
                                                1.63:57.5,
                                                1.64:58.2,
                                                1.65:58.9,
                                                1.66:59.6,
                                                1.67:60.7,
                                                1.68:61.5,
                                                1.69:62.2,
                                                1.7:62.8,
                                                1.71:63.6,
                                                1.72:64.3,
                                                1.73:69.1,
                                                1.74:69.8,
                                                1.75:66.5,
                                                1.76:67.2,
                                                1.77:67.8,
                                                1.78:68.6,
                                                1.79:69.3,
                                                1.8:70.1,
                                                1.81:70.7,
                                                1.82:71.5,
                                                1.83:72.2,
                                                1.84:72.9,
                                                1.85:73.6,
                                                1.86:79.7,
                                                1.87:80.8,
                                                1.88:81.7,
                                                1.89:82.6,
                                                1.9:83.5,
                                                1.91:84.4,
                                                1.92:85.3,
                                                1.93:86}

    if genero == "Hombre":

        #Comparar la estatura con el peso: Si es mayo es sobre peso
        # print(esta_usuario)
        # print(diccionario_relacion_peso_altura_hombres[float(esta_usuario)])
        # print(peso_usuario)
        if peso_usuario > diccionario_relacion_peso_altura_hombres[float(esta_usuario)]:

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

    print("\n--------------- Menu de registro de Raxnaquil ---------------\n")

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
