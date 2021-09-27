def inicio():
    opt = '''
    ¡Empecemos!...
    Escoje una opción\n

    [1] Iniciar Sesión\n
    [2] Registrarse\n
    '''
    print(opt)

    opt_1 = input('Escribe el numero de opción que elejiste\n')

    if (opt_1 == '1'):
        nombre = input("Nombre de usuario\n")
        contraseña = input("Contraseña\n")
        listdata = []
        with open('database.txt') as file_object:
            for line in file_object:
                listdata.append(line.rstrip())
            if nombre in listdata:
                userdata = []
                database_1 = (nombre+'.txt')
                with open(database_1) as file_object:
                    for line in file_object:
                        userdata.append(line.rstrip())
                    if contraseña == userdata[0]:
                        print('bienvenido')
            else:
                print('El usuario no existe')
                

    else:
        nombre = input('Ingrese su nombre de usuario\n')
        listdata = []
        with open('database.txt') as file_object:
            for line in file_object:
                listdata.append(line.rstrip())
            if nombre in listdata:
                msgingreso = 'Este usario ya existe'      
            else:
                contraseña = input('Ingrese su contraseña\n')
                if len(contraseña) < 8:
                    msgingreso = ('Contraseña corta')
                    print(msgingreso)
                    

                else:
                    with open('database.txt', 'a') as file_object: 
                        file_object.write(nombre)
                        file_object.write("\n")
                    f= open(nombre+".txt","w+")
                    f.write(nombre)
                    f.write("\n")
                    f.write(contraseña)
                    f.write("\n")
                    

