# Encabezo

from Usuario import Doctor, Paciente, Usuario, Calificaciones

import Vista

# import pandas as pd
# import csv

lista_doctores = []
lista_pacientes = []

def menu_doctor(doctor):
    # print("[ 1 ] observar reseñas")
    # print("[ 2 ] mirar pacientes")
    while(True):
        respuesta = Vista.menu_loggeo_doctor()
        
        if respuesta == "1":
            # El docotor puede ver su las reseñas que dejaron sus pacientes:
            print("Para comenzar, porfavor ingrese el carnet del doctor del que desea tener información:")

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
    
            if doctor_econtrado:
                calificaciones = "calificaciones.csv"
                with open(calificaciones, "r") as archivo:
                    for linea in archivo:
                        linea = linea.rstrip()
                        separador = ","
                        lista = linea.split(",")
                        cal = lista[1]
                        print("\nLa calificacion y comentarios para el Dr." + apellido + "es: " + cal + "\n")

                pass

            else:

                print("\n ! El doctor no ha sido encontrado, porfavor intenta de nuevo..\n")
            
            pass

        elif respuesta == "2":
            # Mirar pacientes atendidos
            pass
    #pass

def menu_paciente(paciente):
    # print("[ 1 ] Modificar sintoma")
    # print("[ 2 ] Buscar doctor")
    # print("[ 3 ] Modificar mi presupuesto")
    # print("[ 4 ] Calificar a un doctor")
    # print("[ 5 ] Cerrar mi sesion\n")
    while(True):
        respuesta = Vista.menu_loggeo_paciente()


        if respuesta == "1":
            # El paciente modificara su sintoma:
            paciente.sintoma_paciente = Vista.elegir_sintoma_usuario()
            Vista.avisar_nuevo_sintoma(paciente.sintoma_paciente)
            pass



        elif respuesta == "2":

            # El paciente buscara un doctor:
            doctor_encontrado = False
            lista_doctores_temp = []
            # Crear una lista con todos los doctores disponibles:
            f = open("datosDoctores.csv", "r")
            for doc in f.readlines():
                # print("Usuario encontrado")
                dnd = doc.replace("\n","").split(",")
                D = Doctor(dnd[0],dnd[1],dnd[2],dnd[3],dnd[4],dnd[5],dnd[6],dnd[7])
                lista_doctores_temp.append(D)

            # Una vez que ya tenemos a todos los doctores los comparamos uno a uno con las necesidades del paciente

            for doctor in lista_doctores_temp:
                if str(doctor.especialidad_doctor).replace("\n","") == str(paciente.sintoma_paciente).replace("\n",""):

                    # print(doctor.ubicacion_usuario + " " + paciente.ubicacion_usuario)
                    if doctor.ubicacion_usuario == paciente.ubicacion_usuario:

                        if int(paciente.presupuesto_paciente) - int(doctor.precio_consulta) > 0:

                            # print("Paciente emparejado con doctor! " + paciente.nombre_usuario + " " + doctor.nombre_usuario )
                            # (nombrepaciente, nombredoctor , carnetdoctor , ubi):

                            nombre_paciente = str(paciente.nombre).capitalize() + " " + str(paciente.apellido).capitalize()
                            nombre_doctor   = str(doctor.nombre).capitalize() + " " + str(doctor.apellido).capitalize()
                            carnet_doctor   = str(doctor.carnet_doctor)
                            ubicacion       = str(paciente.ubicacion_usuario)
                            precio_consulta = str(doctor.precio_consulta)
                            Vista.paciente_encontrado_doctor(nombre_paciente,nombre_doctor,carnet_doctor,ubicacion,precio_consulta)
                            doctor_encontrado = True

                            # Escribimos el match en las relaciones de doctores:

                            with open("relacionesdoctor.csv","a") as archivo:
                                archivo.write(str(doctor.nombre_usuario) + "," + str(paciente.nombre_usuario) + "\n")

                            # Nos salimos para asegurar que no empareje a otro doctor:
                            break

            if doctor_encontrado == False:
                print("\nNo se ha podido localizar un doctor con tu sintoma y ubicacion, porfavor intenta mas tarde...\n")



        elif respuesta == "3":
            # El paciente modificara su sintoma:
            paciente.presupuesto_paciente = Vista.elegir_presupuesto_usuario()
            Vista.avisar_nuevo_presupuesto(paciente.presupuesto_paciente)
            pass



        elif respuesta == "4":

            # Deja una calificacion:
            Vista.dejar_calificacion()

            pass

        elif respuesta == "5":

            # Generar la olla alimenticia:
            Vista.generar_olla_alimenticia_usuario(paciente=paciente)
            pass

        else:

            # Se desloggea:
            break

def iniciar_sesion():

    datos = Vista.pedir_datos_loggeo()
    usuario = datos[0]
    clave = datos[1]

    D = None
    P = None

    f = open("datosDoctores.csv", "r")
    for i in f.readlines():
        if usuario == i.split(",")[0] and clave == i.split(",")[1]:

            # print("Usuario encontrado")
            dnd = i.split(",")
            D = Doctor(dnd[0],dnd[1],dnd[2],dnd[3],dnd[4],dnd[5],dnd[6],dnd[7])
    f = open("datosPacientes.csv", "r")
    for i in f.readlines():
        if usuario == i.split(",")[0] and clave == i.split(",")[1]:

            # print("Usuario encontrado")
            dnp = i.split(",")
            P = Paciente(dnp[0],dnp[1],dnp[2],dnp[3],dnp[4],dnp[5],dnp[6],dnp[7],dnp[8],dnp[9])

    if D == None and P == None:
        # No se encontro el usuario:
        print("\n ! Usuario no encontrado, porfavor intenta de nuevo...")
    elif D != None:
        # Se encontro a un doctor:
        menu_doctor(D)
        pass
    elif P != None:
        # Se encontro a un paciente:
        menu_paciente(P)
        pass
    pass

def registrar_usuario():

    global lista_doctores
    global lista_pacientes

    tipo = Vista.preguntar_tipo_usuario()

    # Leemos el csv de usuarios para generar uno nuevo:

    dato = open("usuariosgenerados.txt","r").read()

    # Usuario actual:

    numero = dato

    # El usuario deicidio registrar un  nuevo doctor:

    if tipo == "1":

        dnd = Vista.recaudar_datos_doctor(numero)

        lista_doctores.append(Doctor(dnd[0],dnd[1],dnd[2],dnd[3],dnd[4],dnd[5],dnd[6],dnd[7]))

        # with open("test.txt", "a") as myfile:
        #     yfile.write("appended text")

        with open("datosDoctores.csv","a") as archivo:
            archivo.write(lista_doctores[0].recaudar_datos_doctor())
        lista_doctores.clear()

    # El usuario deicidio registrar un  nuevo paciente:
    else:

        dnp = Vista.recaudar_datos_paciente(numero)

        lista_pacientes.append(Paciente(dnp[0],dnp[1],dnp[2],dnp[3],dnp[4],dnp[5],dnp[6],dnp[7],dnp[8],dnp[9]))

        with open("datosPacientes.csv","a") as archivo:
            archivo.write(lista_pacientes[0].recaudar_datos_paciente())
        lista_pacientes.clear()

    # with open("usuariosgenerados.csv", "w") as archivo:
    #     escritor = csv.writer(archivo)
    #     escritor.writerows(str(int(numero) + 1))
    file = open("usuariosgenerados.txt","w")
    file.write(str(int(numero) + 1))
    file.close()

def inicio_programa():

    continuidad = True
    while(continuidad):
        respuesta = Vista.menu_principal()
        
        # El usuario eligio iniciar sesion:
        if respuesta == "1":

            iniciar_sesion()

        # El usuario deicidio registrase:
        else:

            registrar_usuario()


if __name__ == "__main__":

    # (self, nombre_usuario , clave , nombre , apellido , ubicacion):

    # U1 = Usuario("20053","1234","Luis","Perez","Zona 16")

    # print(U1.apellido_usuario)

    # D1 = Doctor("2000","1234","Andres","Iniesta","Zona 14", "111","30","Cirujano")

    # print(D1.carnet_doctor)

    inicio_programa()


# (nombre_usuario) (clave) Nombre - Apellido - Carnet - Precio Cobra / consulta - Especialidad - Ubicacion

# (nombre_usuario) (clave) Nombre - Apellido - Edad - Presupuesto - Estatura - Peso (Kg) - Sintomas - Ubicacion