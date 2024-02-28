# Importar las librerías
import filecmp
import json
import mysql.connector
import pandas as pd

# Conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="root",
    database="diccionario_db",
)

# Crear un cursor
cursor = conn.cursor()

# Cargar datos del archivo JSON
with open("diccionario_maya.json", 'r' encoding="utf-8") as file:
    diccionario_data = json.load(file)

# Recorrer el diccionario y insertar datos en la base de datos
for palabra in diccionario_data.keys():
    maya = maya
    español = palabra[español]

    # Insertar la palabra en la base de datos
    insert_query = "INSERT INTO diccionario_json (maya, español) VALUES (%s, %s)"
    cursor.execute(insert_query, (maya, español))

# Confirmar los cambios
conn.commit()

cursor = conn.cursor()
cursor.execute("SELECT maya, espanol from diccionario_json")
resultados = cursor.fetchall()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()




