import tkinter

from Usuario import Doctor, Paciente, Usuario, Calificaciones
from Vista import menu_principal, pedir_datos_loggeo, paciente_encontrado_doctor, elegir_sintoma_usuario, elegir_presupuesto_usuario, dejar_calificacion, elegir_especialidad_doctor, generar_olla_alimenticia_usuario, menu_loggeo_paciente, menu_loggeo_doctor, recaudar_datos_doctor, avisar_nuevo_sintoma, avisar_nuevo_presupuesto, recaudar_datos_paciente, preguntar_tipo_usuario
from main import menu_doctor, menu_paciente, iniciar_sesion, registrar_usuario, inicio_programa
 
ventana = tkinter.Tk()
ventana.geometry("380x300")

def Ingresarusuario():
    pedir_datos_loggeo()

def Registrarusuario():
    preguntar_tipo_usuario()
boton2 = tkinter.Button(ventana, text = "Registrar usuario", command = Registrarusuario)
boton2.pack()

ventana.mainloop()