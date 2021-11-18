import tkinter as tk
import sys
from typing import Text
from tkinter import Entry, OptionMenu, StringVar, messagebox
import random
class Usuario:

    # Lugar para definir variable no existe

    # Pero si tienen (nombre_usuario) (clave) Nombre - Apellido - Ubicacion | en comun

    def __init__(self, nombre_usuario , clave , nombre , apellido , ubicacion):

        self.nombre_usuario    = nombre_usuario
        self.clave_ingreso     = clave
        self.nombre            = nombre
        self.apellido          = apellido
        self.ubicacion_usuario = ubicacion


class Doctor(Usuario):

    # Clase de Doctor: Carnet - Precio Cobra / consulta - Especialidad

    def __init__(self, nombre_usuario, clave, nombre, apellido, ubicacion, carnet, precio , especialidad):
        super().__init__(nombre_usuario, clave, nombre, apellido, ubicacion)

        self.carnet_doctor       = carnet
        self.precio_consulta     = precio
        self.especialidad_doctor = especialidad

    def recaudar_datos_doctor(self):
        return self.nombre_usuario + "," + self.clave_ingreso + "," + self.nombre+ "," + self.apellido + "," + self.ubicacion_usuario + "," + self.carnet_doctor + "," + self.precio_consulta + "," + self.especialidad_doctor + "\n"

class Paciente(Usuario):

    # Clase de paciente: Edad - Presupuesto - Estatura - Peso (Kg) - Sintomas

    def __init__(self, nombre_usuario, clave, nombre, apellido, ubicacion, edad, presupuesto, estatura, peso, sintoma):
        super().__init__(nombre_usuario, clave, nombre, apellido, ubicacion)

        self.edad_paciente        = edad
        self.presupuesto_paciente = presupuesto
        self.estatura_paciente    = estatura
        self.peso_paciente        = peso
        self.sintoma_paciente     = sintoma

    def recaudar_datos_paciente(self):
        return self.nombre_usuario + "," + self.clave_ingreso + "," + self.nombre + "," + self.apellido+ "," + self.ubicacion_usuario  + "," + self.edad_paciente  + "," + self.presupuesto_paciente  + "," + self.estatura_paciente  + "," + self.peso_paciente  + "," + self.sintoma_paciente + "\n"

class Calificaciones(Usuario):
    
    # Clase de reseñas: carnet - reseña
    
    def __init__(self, carnet, calificacion):
        
        self.carnet_d_doctor       = carnet
        self.calificacion_d_doctor = calificacion


# Setup de la venta 
root = tk.Tk()
root.title("Proyecto Final POO")
root.geometry('400x400')
root.configure(background='white')
root.resizable(0,0)

# Aqui van los metodos:

def ingresar_usuario():
    
    # Se oculta
    root.withdraw()

    D = None
    P = None

    v_ingresar_u = tk.Tk()
    v_ingresar_u.title("Proyecto Final POO")
    v_ingresar_u.geometry('400x400')
    v_ingresar_u.configure(background='white')
    v_ingresar_u.resizable(0,0)
    
    usuario = tk.StringVar(v_ingresar_u)
    clave = tk.StringVar(v_ingresar_u)
    
    def menu_doctor(doctor):
        
        v_ingresar_u.withdraw()
        
        v_md = tk.Tk()
        v_md.title("Proyecto Final POO")
        v_md.geometry('400x400')
        v_md.configure(background='white')
        v_md.resizable(0,0)
        
        caja_texto = tk.Text(v_md)
        
        def desloggear():
            v_ingresar_u.deiconify()
            v_md.withdraw()
            pass
        
        def observar_resenas():
            calificaciones = "calificaciones.csv"
            resenas = ""
            with open(calificaciones, "r") as archivo:
                for linea in archivo:
                    linea = linea.rstrip()
                    separador = ","
                    lista = linea.split(",")
                    cal = lista[1]
                    resenas = resenas + "\n" + cal
                    # print("\nLa calificacion y comentarios para el Dr. es: " + cal + "\n")
            caja_texto.insert(tk.INSERT, resenas)
            pass
        
        def observar_pacientes():
            relacionesdoctor = "relacionesdoctor.csv"
            paciente = ""
            with open(relacionesdoctor, "r") as archivo:
                for linea in archivo:
                    linea = linea.rstrip()
                    separador = ","
                    lista = linea.split(",")
                    cal = lista[1]
                    paciente = paciente + "\n" + cal
                    # print("\nLos pacientes que atendio el Dr. son: "+ cal + "\n")
            caja_texto.insert(tk.INSERT, paciente)
            pass
        
        texto_menu_doctor = tk.Label(v_md, text="Menu de Doctor de Raxnaquil")
        texto_menu_doctor.config(font=("Helvetica",18))
        
        b_observa_res = tk.Button(v_md, text="Observar reseñas", command= observar_resenas, height= 3, width=15)
        b_observar_pacientes = tk.Button(v_md, text="Observar pacientes", command= observar_pacientes, height= 3, width=15)
        b_regresar_md = tk.Button(v_md, text="Desloggear", command= desloggear, height= 3, width=15)
    
        texto_menu_doctor.pack()
        b_observa_res.pack(pady=10)
        b_observar_pacientes.pack(pady=10)
        b_regresar_md.pack(pady=10)
        caja_texto.pack(pady=10)
        pass
    
    def menu_paciente(paciente):
        
        v_ingresar_u.withdraw()
        
        v_mp = tk.Tk()
        v_mp.title("Proyecto Final POO")
        v_mp.geometry('400x650')
        v_mp.configure(background='white')
        v_mp.resizable(0,0)
        
        ddsintoma = StringVar(v_mp)
        ddgenero = StringVar(v_mp)
        caja_texto = tk.Text(v_mp)
        presupuesto = tk.StringVar(v_mp)
        
        # Metodos aqui
        
        def desloggear():
            v_ingresar_u.deiconify()
            v_mp.withdraw()
            pass
        
        def aplicar_cambios():
            messagebox.showinfo("Cambios aplicados","Sus cambios han sido aplicados a su instancia!")
            pass
        
        def generar_olla():
            
            presupuesto_para_carnes = (int(paciente.presupuesto_paciente) / 8)
            presupuesto_para_lacteos = (int(paciente.presupuesto_paciente) / 8)
            presupuesto_para_cereales = (int(paciente.presupuesto_paciente) / 8) * 4
            presupuesto_para_verfruts = (int(paciente.presupuesto_paciente) / 8) * 2

            peso_usuario = int(paciente.peso_paciente)
            esta_usuario = paciente.estatura_paciente

            diccionario_relacion_peso_altura_hombres = {1.75:58.1,
                                                        1.58:54.8}
            diccionario_relacion_peso_altura_mujeres = {1.57:53.7,
                                                        1.75:54.3}

            caja_texto.delete("1.0", tk.END)
            
            if ddgenero.get() == "Hombre":

                #Comparar la estatura con el peso: Si es mayo es sobre peso
                # print(esta_usuario)
                # print(diccionario_relacion_peso_altura_hombres[float(esta_usuario)])
                # print(peso_usuario)
                if peso_usuario > diccionario_relacion_peso_altura_hombres[float(esta_usuario)]:

                    # Tiene sobre peso haga ejercicio:

                    caja_texto.insert(tk.INSERT, "Se le recomienda hacer ejercicio para bajar un poco su peso. Visite la siguiente pagina para tener una guia de como hacerlo: URL")
                    
            
                else:

                    # Si cumple con el peso indicado, ponerle su dieta:

                    lista_carnes = [["Res",13],["Pollo",12],["Cerdo",10]] # La suma de dos precios no puede ser mayor a 25
                    lista_lactes = [["Leche",10],["Queso",10],["Yougurt",5]]
                    lista_carboh = [["Arroz",4],["Maiz",4.5],["Frijol",4]] # No se puede pasar de 4.75
                    lista_verfru = [["Banano",3],["Aguacate",4],["Sandia",7]] # No se puede pasar de 7Q

                    caja_texto.insert(tk.INSERT,"Imprimiendo olla alimenticia de esta semana de acorde a su presupuesto: ")
                    caja_texto.insert(tk.INSERT,"Listando sus 2 porciones de carnes a la semana:")
                    for i in range(2):
                        carne_electa = lista_carnes[random.randint(0,len(lista_carnes) - 1)]
                        caja_texto.insert(tk.INSERT,str(i + 1) + " " + carne_electa[0] + " Precio: " + str(carne_electa[1]))
                    caja_texto.insert(tk.INSERT,"Listando sus 3 porciones de lacteos a la semana:")
                    for i in range(3):
                        lacteo_electo = lista_lactes[random.randint(0,len(lista_lactes)- 1)]
                        caja_texto.insert(tk.INSERT,str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
                    caja_texto.insert(tk.INSERT,"Listando sus 21 porciones de carbohidratos a la semana:")
                    diccionario_carbo = {}
                    for i in range(len(lista_carboh)):
                        diccionario_carbo[lista_carboh[i][0]] = 0
                    for i in range(21):
                        carboh_electo = lista_carboh[random.randint(0,len(lista_carboh)- 1)]
                        diccionario_carbo[carboh_electo[0]] = diccionario_carbo[carboh_electo[0]] + 1
                        # print(str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
                    caja_texto.insert(tk.INSERT,str(diccionario_carbo))
                    caja_texto.insert(tk.INSERT,"Listando sus 7 porciones de frutas y verduras a la semana:")
                    for i in range(7):
                        frutaver_electa = lista_verfru[random.randint(0,len(lista_verfru)- 1)]
                        caja_texto.insert(tk.INSERT,str(i + 1) + " " + frutaver_electa[0] + " Precio: " + str(frutaver_electa[1]))
                        
            if ddgenero.get() == "Mujer":

                #Comparar la estatura con el peso: Si es mayo es sobre peso
                if peso_usuario > diccionario_relacion_peso_altura_mujeres[float(esta_usuario)]:

                    # Tiene sobre peso haga ejercicio:

                    caja_texto.insert(tk.INSERT, "Se le recomienda hacer ejercicio para bajar un poco su peso. Visite la siguiente pagina para tener una guia de como hacerlo: URL")


                else:
                    # Si cumple con el peso indicado, ponerle su dieta:

                    lista_carnes = [["Res",13],["Pollo",12],["Cerdo",10]] # La suma de dos precios no puede ser mayor a 25
                    lista_lactes = [["Leche",10],["Queso",10],["Yougurt",5]]
                    lista_carboh = [["Arroz",4],["Maiz",4.5],["Frijol",4]] # No se puede pasar de 4.75
                    lista_verfru = [["Banano",3],["Aguacate",4],["Sandia",7]] # No se puede pasar de 7Q

                    caja_texto.insert(tk.INSERT,"Imprimiendo olla alimenticia de esta semana de acorde a su presupuesto: ")
                    caja_texto.insert(tk.INSERT,"Listando sus 2 porciones de carnes a la semana:")
                    for i in range(2):
                        carne_electa = lista_carnes[random.randint(0,len(lista_carnes) - 1)]
                        caja_texto.insert(tk.INSERT,str(i + 1) + " " + carne_electa[0] + " Precio: " + str(carne_electa[1]))
                    caja_texto.insert(tk.INSERT,"Listando sus 3 porciones de lacteos a la semana:")
                    for i in range(3):
                        lacteo_electo = lista_lactes[random.randint(0,len(lista_lactes)- 1)]
                        caja_texto.insert(tk.INSERT,str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
                    caja_texto.insert(tk.INSERT,"Listando sus 21 porciones de carbohidratos a la semana:")
                    diccionario_carbo = {}
                    for i in range(len(lista_carboh)):
                        diccionario_carbo[lista_carboh[i][0]] = 0
                    for i in range(21):
                        carboh_electo = lista_carboh[random.randint(0,len(lista_carboh)- 1)]
                        diccionario_carbo[carboh_electo[0]] = diccionario_carbo[carboh_electo[0]] + 1
                        # print(str(i + 1) + " " + lacteo_electo[0] + " Precio: " + str(lacteo_electo[1]))
                    caja_texto.insert(tk.INSERT,str(diccionario_carbo))
                    caja_texto.insert(tk.INSERT,"Listando sus 7 porciones de frutas y verduras a la semana:")
                    for i in range(7):
                        frutaver_electa = lista_verfru[random.randint(0,len(lista_verfru)- 1)]
                        caja_texto.insert(tk.INSERT,str(i + 1) + " " + frutaver_electa[0] + " Precio: " + str(frutaver_electa[1]))
            
            pass
        
        def emparejar_doctor():
            
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
                            # Vista.paciente_encontrado_doctor(nombre_paciente,nombre_doctor,carnet_doctor,ubicacion,precio_consulta)
                            # print("Departamento: " + str(ubi.split("-")[1]).upper() + " | " + "Zona: " + str(ubi.split("-")[0]))
                            # print("\nPerfecto " + nombrepaciente + ", hemos encontrado al doctor " + nombredoctor + " que te antendera con gusto.")
                            # print("Porfavor refierete a el en el hospital con su numero de carnet: " + carnetdoctor + " | Precio por consulta: " + precio + "$\n")
                            caja_texto.delete("1.0", tk.END)
                            texto_ = "Departamento: " + str(ubicacion.split("-")[1]).upper() + " | " + "Zona: " + str(ubicacion.split("-")[0])
                            texto_ = texto_ + "\n" + "Perfecto " + nombre_paciente + ", hemos encontrado al doctor " + nombre_doctor + " que te antendera con gusto."
                            texto_ = texto_ + "\n" + "Porfavor refierete a el en el hospital con su numero de carnet: " + carnet_doctor + " | Precio por consulta: " + precio_consulta + "$"
                            caja_texto.insert(tk.INSERT, texto_)
                            
                            doctor_encontrado = True

                            # Escribimos el match en las relaciones de doctores:

                            with open("relacionesdoctor.csv","a") as archivo:
                                archivo.write(str(doctor.nombre_usuario) + "," + str(paciente.nombre_usuario) + "\n")

                            # Nos salimos para asegurar que no empareje a otro doctor:
                            break

            if doctor_encontrado == False:
                
                caja_texto.insert(tk.INSERT, "No se ha podido localizar un doctor con tu sintoma y ubicacion, porfavor intenta mas tarde...")
            
            pass
        
        
        ddsintoma.set(paciente.sintoma_paciente)
        
        ddgenero.set("Hombre")
        
        tag_sintoma = tk.Label(v_mp, text="Sintoma")
        tag_presupuesto = tk.Label(v_mp, text="Presupuesto")
        
        ddgenero_tk = OptionMenu(v_mp, ddgenero, "Hombre","Mujer")
        
        ddsintoma_tk = OptionMenu(v_mp, ddsintoma, "Cabeza","Cuello","Pecho","Dorso","Espalda","Cintura","Pierna","Brazo","Pie","Mano","Otros")
        
        b_emparejar_paciente = tk.Button(v_mp, text="Buscar Doctor", command= emparejar_doctor, height= 3, width=15)
        
        b_regresar_mp = tk.Button(v_mp, text="Desloggear", command= desloggear, height= 3, width=15)
        
        b_generar_o_mp = tk.Button(v_mp, text="Generar Olla", command= generar_olla, height= 3, width=15)
        
        b_aplicar_cambios_mp = tk.Button(v_mp, text="Aplicar Cambios", command= aplicar_cambios, height= 3, width=15)
        
        ct_presupuesto = tk.Entry(v_mp, justify="center", textvariable= presupuesto)
        ct_presupuesto.insert(0,paciente.presupuesto_paciente)
        
        
        # Botones y el resto aqui:
        
        texto_menu_paciente = tk.Label(v_mp, text="Menu de Paciente de Raxnaquil")
        texto_menu_paciente.config(font=("Helvetica",18))
        
        
        texto_menu_paciente.pack()
        
        tag_sintoma.pack(pady=10)
        
        ddsintoma_tk.pack()
        
        ddgenero_tk.pack()
        
        tag_presupuesto.pack(pady=10)
        
        ct_presupuesto.pack()
        
        b_emparejar_paciente.pack(pady=10)
        
        b_generar_o_mp.pack(pady=10)
        
        b_aplicar_cambios_mp.pack(pady=10)
        
        b_regresar_mp.pack(pady=10)
        
        caja_texto.pack(pady=10)
        
        pass
    
    
    
    def boton_mostrar_menu_principal():
        
        v_ingresar_u.withdraw()
        root.deiconify()
        
        pass
    
    def intentar_loggeo():
        
        D = None
        P = None

        f = open("datosDoctores.csv", "r")
        for i in f.readlines():
            if usuario.get() == i.split(",")[0] and clave.get() == i.split(",")[1]:

                # print("Usuario encontrado")
                dnd = i.split(",")
                D = Doctor(dnd[0],dnd[1],dnd[2],dnd[3],dnd[4],dnd[5],dnd[6],dnd[7])
        f = open("datosPacientes.csv", "r")
        for i in f.readlines():
            if usuario.get() == i.split(",")[0] and clave.get() == i.split(",")[1]:

                # print("Usuario encontrado")
                dnp = i.split(",")
                P = Paciente(dnp[0],dnp[1],dnp[2],dnp[3],dnp[4],dnp[5],dnp[6],dnp[7],dnp[8],dnp[9])
        
        if D == None and P == None:
            # No se encontro el usuario:
            # print("! Usuario no encontrado, porfavor intenta de nuevo...")
            messagebox.showerror("Usuario no encontrado","El usuario o la clave no fueron reconocidos, intenta de nuevo...")
            
        elif D != None:
            # Se encontro a un doctor:
            # print("Se encontro doctor")
            menu_doctor(D)
            pass
        elif P != None:
            # Se encontro a un paciente:
            # print("Se encontro paciente")
            menu_paciente(P)
            pass
        pass
    
    
    
    
    texto_menu_ingresar = tk.Label(v_ingresar_u, text="Menu de loggeo de Raxnaquil")
    texto_menu_ingresar.config(font=("Helvetica",18))
    
    
    
    ct_usuario = tk.Entry(v_ingresar_u, justify="center", textvariable= usuario)
    ct_usuario.insert(0,"Usuario")
    
    ct_clave = tk.Entry(v_ingresar_u, justify="center", textvariable= clave)
    ct_clave.insert(0,"Clave")
    
    
    b_regresar = tk.Button(v_ingresar_u, text="Regresar", command= boton_mostrar_menu_principal, height= 3, width=15)
    b_ingresar = tk.Button(v_ingresar_u, text="Ingresar", command= intentar_loggeo, height= 3, width=15)
    
    
    texto_menu_ingresar.pack()
    ct_usuario.pack(pady=30)
    ct_clave.pack(pady=30)
    b_ingresar.pack(pady=10)
    b_regresar.pack(pady=10)
    v_ingresar_u.mainloop()
    
    pass

def registrar_usuario():
    
    # Primero cerramos la primera venta creada:
    
    root.withdraw()

    # Creamos la nueva ventana donde le preguntamos si es usuario o doctor:
    ven_registrar = tk.Tk()
    ven_registrar.title("Proyecto Final POO")
    ven_registrar.geometry('400x400')
    ven_registrar.configure(background='white')
    ven_registrar.resizable(0,0)
    
    # En esta parte iran las funciones para cada boton del menu de registro:
    
    def registrar_nuevo_doctor():
        
        # Comenzamos el registro de un nuevo doctor:
        # Ocultamos la ventana anterior:
        
        ven_registrar.withdraw()
        
        # Creamos una nueva ventana para el registro del doctor:
        
        ven_registrar_doctor = tk.Tk()
        ven_registrar_doctor.title("Proyecto Final POO")
        ven_registrar_doctor.geometry('400x400')
        ven_registrar_doctor.configure(background='white')
        ven_registrar_doctor.resizable(0,0)
        
        # Creamos las variables que utilizaremos:
        
        nom_doc = tk.StringVar(ven_registrar_doctor)
        
        clv_doc = tk.StringVar(ven_registrar_doctor)
        
        crt_doc = tk.StringVar(ven_registrar_doctor)
        
        pre_doc = tk.StringVar(ven_registrar_doctor)
        
        esp_doc = tk.StringVar(ven_registrar_doctor)
        
        esp_doc.set("Cabeza")
        
        zon_doc = tk.StringVar(ven_registrar_doctor)
        
        zon_doc.set("1")
        
        # Aqui iran los metodos:
        
        def registrar_nuevo_doctor_():
            # return self.nombre_usuario + "," + self.clave_ingreso + "," + self.nombre+ "," + self.apellido + "," + self.ubicacion_usuario + "," + self.carnet_doctor + "," + self.precio_consulta + "," + self.especialidad_doctor + "\n"
            # Guardando los datos:
            dato = open("usuariosgenerados.txt","r").read()
            file = open("usuariosgenerados.txt","w")
            file.write(str(int(dato) + 1))
            file.close()
            datos_temporales = (nom_doc.get()[0] + nom_doc.get()[0] + dato) + "," + clv_doc.get() + "," + nom_doc.get().split(" ")[0]  + "," + nom_doc.get().split(" ")[1] + "," + (zon_doc.get() +"-Guatemala") + "," + crt_doc.get() + "," + pre_doc.get() + "," + esp_doc.get() + "\n"
            with open("datosDoctores.csv","a") as archivo:
                archivo.write(datos_temporales)
            
            messagebox.showinfo("Completado","Doctor creado con exito con nombre de usuario: " + (nom_doc.get()[0] + nom_doc.get()[0] + dato) + " !")
            ven_registrar_doctor.withdraw()
            ven_registrar.deiconify()
        
        # Aqui van las tags:
        
        label_nuevo_doctor = tk.Label(ven_registrar_doctor, text="Registro de Doctor de Raxnaquil")
        label_nuevo_doctor.config(font=("Helvetica",18))
        
        # Aqui iran los demas componentes:
        
        # Entrada del nombre y apellido:
        ent_nombre_doc = tk.Entry(ven_registrar_doctor, justify="center", textvariable= nom_doc)
        ent_nombre_doc.insert(0,"Nombre y Apellido")
        
        # Entrada de la clave:
        
        ent_clave_doc = tk.Entry(ven_registrar_doctor, justify="center", textvariable= clv_doc)
        ent_clave_doc.insert(0,"Clave")
        
        # Entrada de su carnet:
        
        ent_carnet_doc = tk.Entry(ven_registrar_doctor, justify="center", textvariable= crt_doc)
        ent_carnet_doc.insert(0,"Carnet")
        
        # Entrada del costo:
        
        ent_precio_doc = tk.Entry(ven_registrar_doctor, justify="center", textvariable= pre_doc)
        ent_precio_doc.insert(0,"Precio x Consulta")
        
        # Dropdown de la especialidad:
        
        dd_especialidad_doc = OptionMenu(ven_registrar_doctor, esp_doc, "Cabeza","Cuello","Pecho","Dorso","Espalda","Cintura","Pierna","Brazo","Pie","Mano","Otros")
        
        # Dropdown de la zona:
        
        dd_zona_doc = OptionMenu(ven_registrar_doctor, zon_doc, "1","10","11","12","13","14","15","16","17","20","21")
        
        # Boton de registrar:
        
        b_regitrar_doc = tk.Button(ven_registrar_doctor, text="Registrar", command= registrar_nuevo_doctor_, height= 3, width=15)
        
        # Renderizamos los componentes:
        
        label_nuevo_doctor.pack()
        ent_nombre_doc.pack(pady=10)
        ent_clave_doc.pack(pady=10)
        ent_carnet_doc.pack(pady=10)
        ent_precio_doc.pack(pady=10)
        dd_especialidad_doc.pack(pady=10)
        dd_zona_doc.pack(pady=10)
        b_regitrar_doc.pack(pady=10)
        
        
    def registrar_nuevo_usuario():
        
        # Comenzamos el registro de un nuevo doctor:
        # Ocultamos la ventana anterior:
        
        ven_registrar.withdraw()
        
        # Creamos una nueva ventana para el registro del doctor:
        
        ven_registrar_paciente = tk.Tk()
        ven_registrar_paciente.title("Proyecto Final POO")
        ven_registrar_paciente.geometry('400x400')
        ven_registrar_paciente.configure(background='white')
        ven_registrar_paciente.resizable(0,0)
        
        # Creamos las variables que utilizaremos:
        
        nom_pac = tk.StringVar(ven_registrar_paciente)
        
        clv_pac = tk.StringVar(ven_registrar_paciente)
        
        edd_pac = tk.StringVar(ven_registrar_paciente)
        
        pre_pac = tk.StringVar(ven_registrar_paciente)
        
        est_pac = tk.StringVar(ven_registrar_paciente)
        
        pes_pac = tk.StringVar(ven_registrar_paciente)
        
        sin_pac = tk.StringVar(ven_registrar_paciente)
        
        sin_pac.set("Cabeza")
        
        zon_pac = tk.StringVar(ven_registrar_paciente)
        
        zon_pac.set("1")
        
        # Aqui iran los metodos:
        
        def registrar_nuevo_paciente_():
            
            dato = open("usuariosgenerados.txt","r").read()
            file = open("usuariosgenerados.txt","w")
            file.write(str(int(dato) + 1))
            file.close()
            crnt = nom_pac.get().split(" ")[0][0] + nom_pac.get().split(" ")[1][0] + dato
            clav = clv_pac.get()
            nomb = nom_pac.get().split(" ")[0]
            apel = nom_pac.get().split(" ")[1]
            zona = zon_pac.get() + "-guatemala"
            edad = edd_pac.get()
            pres = pre_pac.get()
            esta = est_pac.get()
            peso = pes_pac.get()
            sint = sin_pac.get()
            
            temp = crnt +","+ clav +","+ nomb +","+ apel +","+ zona +","+ edad +","+ pres +","+ esta +","+ peso +","+ sint +"\n" 
            
            with open("datosPacientes.csv","a") as archivo:
                
                archivo.write(temp)
            
            
            messagebox.showinfo("Completado","Paciente creado con exito con nombre de usuario: " + crnt + " !")
            ven_registrar_paciente.withdraw()
            ven_registrar.deiconify()
        
        # Aqui van las tags:
        
        label_nuevo_doctor = tk.Label(ven_registrar_paciente, text="Registro de Paciente de Raxnaquil")
        label_nuevo_doctor.config(font=("Helvetica",18))
        
        b_regitrar_pac = tk.Button(ven_registrar_paciente, text="Registrar", command= registrar_nuevo_paciente_, height= 3, width=15)
        
        ent_nombre_pac = tk.Entry(ven_registrar_paciente, justify="center", textvariable= nom_pac)
        ent_nombre_pac.insert(0,"Nombre y Apellido")
        
        ent_clave_pac = tk.Entry(ven_registrar_paciente, justify="center", textvariable= clv_pac)
        ent_clave_pac.insert(0,"Clave")
        
        ent_edd_pac = tk.Entry(ven_registrar_paciente, justify="center", textvariable= edd_pac)
        ent_edd_pac.insert(0,"Edad")
        
        ent_pre_pac = tk.Entry(ven_registrar_paciente, justify="center", textvariable= pre_pac)
        ent_pre_pac.insert(0,"Presupuesto")
        
        ent_est_pac = tk.Entry(ven_registrar_paciente, justify="center", textvariable= est_pac)
        ent_est_pac.insert(0,"Estatura")
        
        ent_pes_pac = tk.Entry(ven_registrar_paciente, justify="center", textvariable= pes_pac)
        ent_pes_pac.insert(0,"Peso")
        
        dd_sin_pac = OptionMenu(ven_registrar_paciente, sin_pac, "Cabeza","Cuello","Pecho","Dorso","Espalda","Cintura","Pierna","Brazo","Pie","Mano","Otros")
        
        dd_zona_pac = OptionMenu(ven_registrar_paciente, zon_pac, "1","10","11","12","13","14","15","16","17","20","21")
        
        # Se renderizan:
        
        label_nuevo_doctor.pack()

        
        ent_nombre_pac.pack(pady=8)
        ent_clave_pac.pack(pady=8)
        ent_edd_pac.pack(pady=8)
        ent_pre_pac.pack(pady=8)
        ent_est_pac.pack(pady=8)
        ent_pes_pac.pack(pady=8)
        dd_sin_pac.pack(pady=8)
        dd_zona_pac.pack(pady=8)
        
        b_regitrar_pac.pack(pady=8)
        
        
    
    def regresar():
        
        ven_registrar.withdraw()
        root.deiconify()
        
        pass
    
    
    # Creamos la label del menu:
    
    texto_menu_ingresar = tk.Label(ven_registrar, text="Menu de registro de Raxnaquil")
    texto_menu_ingresar.config(font=("Helvetica",18))
    
    # Creamos los botones para saber cual desea registrar:
    
    b_reg_dc = tk.Button(ven_registrar, text="Nuevo Doctor", command= registrar_nuevo_doctor, height= 3, width=15)
    b_reg_us = tk.Button(ven_registrar, text="Nuevo Usuario", command= registrar_nuevo_usuario, height= 3, width=15)
    b_regresar = tk.Button(ven_registrar, text="Regresar", command= regresar, height= 3, width=15)
    
    # Renderizamos los componentes:
    
    texto_menu_ingresar.pack()
    b_reg_dc.pack(pady=30)
    b_reg_us.pack(pady=30)
    b_regresar.pack(pady=30)
    
    pass

def salir_menu_principal():
    
    sys.exit()



# Aqui van los componentes:

texto_menu = tk.Label(root, text="Menu Principal de Raxnaquil")
texto_menu.config(font=("Helvetica",18))

boton_ingresar_usuario = tk.Button(root, text="Ingresar Usuario", command= ingresar_usuario, height= 3, width=15)
boton_registrar_usuario = tk.Button(root, text="Registrar Usuario", command= registrar_usuario, height= 3, width=15)
boton_salir_menu = tk.Button(root, text="Salir", command= salir_menu_principal, height= 3, width=15)


# Aqui se hacen pack de los componentes:

texto_menu.pack()
boton_ingresar_usuario.pack(pady=30)
boton_registrar_usuario.pack(pady=30)
boton_salir_menu.pack(pady=30)

root.mainloop()


    