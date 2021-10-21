import csv

mydict = {}

with open('diccionario_relacion_peso_altura_mujeres.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

print(dict_from_csv)

