# Importar las librerías
import filecamp
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

# Variabl de consulta a la base de datos
cursor = conn.cursor()

# Cargar datos del archivo JSON
with open("diccionario_maya.json", 'r' encoding="utf-8") as file:
    diccionario_data = json.load(file)

for palabra in diccionario_data.keys():
    maya = maya
    español = palabra[español]
    insert_query = "INSERT INTO diccionario_json (maya, español) VALUES (%s, %s)"
    cursor.execute(insert_query, (maya, español))

conn.commit()
cursor.close()
conn.close()

import mysql.connector
import pandas as pd

#Conectar a la base de datos
conn = ysql.connector.connect(
    host="localhest",
    user="root",
    password="root",
    database="diccionario_db"
)

# Variable de consulta a la base de datos
cursor conn.cursor()

# Cargar datos desde el archivo XLSX
df_excel pd.read_excel('diccionario_maya.xlsx')

for index, row is df_excel.iterrows():
  maya row ('Maya')
  espanol row ['Español']
  insert query "INSERT INTO diccionario xlsx (Maya, espanol) VALUES(%s,%s)"
  cursor.execute(insert query, (maya, espanol))

conn.commit()
cursor.close()
conn.close()

import mysql.connector
import pandas as pd

# Conectar a la base de datos
conn = mysql.connector.connect(
    host= "localhost",
    user= "root".
    password ="root",
    database="diccionario_db"
)

#Variable de consulta a la base de datos
cursor conn.cursor()

cursor.execute("SELECT maya, espanol FROM diccionario_json")

resultados = cursor.fetchall()

for fila in resultados:
    maya, espanol = fila
    print("Maya: (maya), ----- Español: (espanol)")

cursor.close()
conn.close()