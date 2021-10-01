import sqlite3
import csv

#Abrimos el archivo CSV
f=open('C:Pacientesdatos.csv','r') 
#Omitimos la linea de encabezado
next(f, None)
reader = csv.reader(f, delimiter=';')

#Crea la BD en la carpeta donde se encuentra el script
sql = sqlite3.connect('Nombres.db')
cur = sql.cursor()

#Creamos la tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS Pacientesdatos
            (codigo int, nombre text, dirección text, padecimientos text)''')

#Llenamos la BD con los datos del CSV
for row in reader:
    cur.execute("INSERT INTO Pacientesdatos VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))

#Muestro las filas guardadas en la tabla
for row in cur.execute('SELECT * FROM Pacientesdatos'):
    print(row)

#Cerramos el archivo y la conexion a la bd
f.close()
sql.commit()
sql.close()