# Encabezo

def menu_principal():

    # Este es el menu principal del proyecto:

    # Raxnaquil

    print("\n--------------- Menu principal de Raxnaquil ---------------\n")
    print("[ 1 ] Ingresar usuario")
    print("[ 2 ] Registrar usuario")
    print("[ 3 ] Salir")
    print("")

    respuesta = input("Opcion: ")

    while(True):

        if respuesta == "1" or respuesta == "2" or respuesta == "3":

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
    print("[ 5 ] Cerrar mi sesion\n")
    
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
    print("[ 2 ] mirar pacientes")
    print("[ 3 ] Cerrar mi sesion\n")
    
    respuesta = input("Opcion: ")
    
    while(True):
        
        if respuesta in ["1","2","3"]:
            
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