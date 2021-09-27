ficha = 0
F = 0
M = 0
paracetamol = 0
losartal = 0
ibuprofeno = 0
omeprazol = 0
enalapril = 0
while True:
    print("""BIENVENIDO LA SERVICIO DE ATENCIÓN DE URGENCIAS
-------------------------------------
1) Ingresar Ficha del Paciente
2) Actualizar Ficha por el Médico
3) Asignación de Medicamentos
4) Obtención de Estadísticas
5) Salir""")
    print()
    print("Elija una opcion: ")
    a = input()
    if a == '1':
        print("FICHA DE INGRESO")
        import datetime
        x = datetime.datetime.now()
        Fecha_Atención = "%s/%s/%s" % (x.day, x.month, x.year)
        Hora_atención = "%s:%s" % (x.hour, x.minute)
        print("Ingrese su nombre completo porfavor")
        nombrer = input()
        print("Porfavor ingrese los datos del paciente")
        print("Ingrese nombre del paciente")
        nombre = input()
        print("Ingrese Apellido del paciente")
        apellido = input()
        print("Ingrese rut del paciente")
        rut = input()
        print("Ingrese estado civil")
        estadoc = input()
        print("Ingrese domicilio")
        domicilio = input()
        print("Ingrese Fono")
        fono = input()
        print("Ingrese nivel de urgencia")
        urgencia = input()
        print("Ingrese sexo")
        sexo = input().upper()
        if sexo == 'MASCULINO'  or sexo == 'M':
            M = M + 1
        elif sexo == 'FEMENINO' or sexo == 'F':
            F = F + 1
        print("Ingrese edad")
        edad = input()
        print("Ingrese grupo sanguíneo del paciente")
        gsanguineo= input()
        print("Asiste acompañado el paciente? (SI/NO)")
        acompañado = input()
        ficha = ficha + 1
        ficha_f = str(ficha).zfill(3)
        print(f"Ficha Generada = #{ficha_f}")
    elif a == '2':
        print("INFORMACION DE ATENCION")
        print("Nombre completo medico: ")
        medico = input()
        print("Especialidad: ")
        especialidad = input()
        print("Sintomas detectados: ")
        sintomas = input()
        print("Diagnostico")
        diagnostico = input()
        while True:
            print("Reposo (SI/NO)")
            reposo = input().upper()
            if reposo == "SI":
                print("Cantidad de dias")
                dias = input().upper()
                break
            elif reposo == "NO":
                print("No requiere reposo")
                dias = "0"
                break
            else:
                print("Elija si o no:")
    elif a == '3':
        print("Ingrese la cantidad de medicamentos")
        cantidad_med = int(input())
        medicamento_contador = 1
        for contador in range (cantidad_med):
            print(f"""Medicamentos
------------------------------------------
1) Paracetamol
2) Losartan
3) Ibuprofeno
4) Omeprazol
5) Enalapril

Elija medicamento {medicamento_contador}
""")
            medicamento = int(input())
            if medicamento == '1' or medicamento == '2' or medicamento == '3' or medicamento == '4' or medicamento == '5':
                medicamento_contador = medicamento_contador + 1
 
    elif a == '4':
        print("C")
    elif a == '5':
        break
    else:
        a = input("Usted a ingresado un dato invalido, presione enter para reiniciar: ")
 
print("PRESIONE ENTER PARA SALIR")
input()
exit()