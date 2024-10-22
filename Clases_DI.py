# %% 1. Cabecera
"""
Autor: Manuel Benito
Clase: Diseño de interfaces

"""

# %% 2. Importar módulos
# import numpy as np
# import funciones as f
# %% 2. Hola mundo
# print("Hola mundo")
# %% 3. Pedir información
# nombre = input("¿Cuál es tu nombre? ")
# edad = int(input("¿Cuál es tu edad? "))
# if edad > 25:
#     print("Hola te llamas",nombre,"y tienes",edad, "lo que significa que eres un poco viejo")
# else:
#     print("Hola te llamas",nombre,"y tienes",edad, "lo que significa que eres joven")

# %% 4. Chequeo de errores
# nombre = input("¿Cuál es tu nombre? ")
# if nombre.isdigit():
#     print("Error, mete un string")
#     exit()

# #verificar numero
# try:
#     edad = int(input("¿Cual ess tu edad "))
# except ValueError:
#     print("Mete un numero")
#     exit()
# %% 4. Tipos de datos
###############################################################################
# Variables inmodificables #
###############################################################################
"""
int, str, tuplas, float, bool.
"""
# 4.1 int
# a = 10
# b = 10
# # print(id(a),id(b))
# a = 5
# b = a
# # b = 10
# print(a,b)
# print(id(a),id(b))

# 4.2 str

# 4.3 Tuplas
"""
....
"""
# tupla = (1, 2, 3)
# tupla = tupla + (5,)
# # print(tupla)
# # # acceder a los elementos
# # E2 = tupla[1]
# # Primera función


# def calc_suma(a, b):
#     suma = a + b
#     resta = a - b
#     return suma, resta


# resultado = calc_suma(10, -5)

# a, b, c, d = tupla


###############################################################################
# Variables modificables #
###############################################################################
# 1. Listas
# lista = [1, 2, 3, 4]
# E0 = print(lista[0])

# lista_anidada = [1, 2, 3, [4, 5, [6, 7]]]
# print(lista_anidada[3][2][1])
# Añadir un valor--> append
# lista = [1, 2, 3, 4]
# lista.append(5)
# for elemento in lista:
#     print(elemento)
############################## Ejercicio de clase #############################
# A pelo
# n_filas1, n_columnas1 = 4, 2
# n_filas2, n_columnas2 = 2, 2
# n_filas3, n_columnas3 = 4, 3
# M = []  # Inicializamos matriz
# c = 1
# for i in range(n_filas1):
#     filai1 = []
#     for j in range(n_columnas1):
#         filai1.append(c)
#         c += 1
#     M.append(filai1)
# Forma bonita
# M = [[0 for _ in range(n_columnas1)]
#      for _ in range(n_filas1)]
# for i in range(n_filas1):
#     for j in range(n_columnas1):
#         M[i][j] = [[0 for _ in range(n_columnas2)] for _ in range(n_filas2)]
#         for ii in range(n_filas2):
#             for jj in range(n_columnas2):
#                 M[i][j][ii][jj] = [
#                     [0 for _ in range(n_columnas3)] for _ in range(n_filas3)]
#                 c = 1
#                 for iii in range(n_filas3):
#                     for jjj in range(n_columnas3):
#                         M[i][j][ii][jj][iii][jjj] = c
#                         c += 1
# Numpy
# Matriz_numpy = np.arange(1, n_filas1 * n_columnas1 *
#                          n_filas2 * n_columnas2 * n_filas3 * n_columnas3 + 1)
# Matriz_numpy = np.reshape(
#     Matriz_numpy, (n_filas1, n_columnas1, n_filas2, n_columnas2, n_filas3, n_columnas3))
# Diccionarios
# diccionario = {"nombre": "Sebastian", "edad": 19}
# print(diccionario["edad"])
# # es modificable
# diccionario["gusto"] = "jugar al Cs2"
# diccionario = {"nombre": "Sebastian", "edad": 19, "Estudios": ["ESO", "SMR"]}
# Claves = diccionario.keys()
# empleados = {
#     "empleado 1": {"nombre": "Sebastian", "Nota": -2},
#     "empleado 2": {"nombre": "Javi", "Nota": 1.5}}
# Conjuntos
# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}
# interseccion = conjunto1.intersection(conjunto2)
# booleano = 5 > 3
# %% 3. Condicionales
# x = 10
# if x > 10:
#     print(f"10 es menor que {x}")
# elif x == 10:
#     print(f"Es igual a 10")
# else:
#     print(f"{x} es menor que 10 ")
# en una sola linea
# x = 5
# print(f"{x} es mayor que 5" if x > 5 else f"{x} es menor o igual que 5")
# condicional y listas
# colores = ["rojo", "verde", "azul", "amararillo",
#            "rojo", "verde", "azul", "amararillo", "rojo"]
# color = "rojo"
# if color in colores:
#     print(f"El color {color} esta dentro de la lista {colores} y está dentro la lista {colores.count(color)}")

""" Switch-case--> match-case"""
# animal = "perro"
# match animal:
#     case"gato"
""" Condicionales con diccionarios """
# diccionario = {"Sebastian": 19,
#                "daniel": 21,
#                "Javier": 19,
#                "Manu": 26,
#                "Ana": 8}
# for persona in diccionario:
#     if diccionario[persona] >= 18:
#         print(f"{persona} es mayor de edad")
#     else:
#         print(f"{persona} no es mayor de edad")

# all(and) y any(or)
# all
# x, y, z = -5, 10, 15
# if all([x > 0, y > 0, z > 0]):
#     print(f"todos son mayores que 0")
# else:
#     print(f"no todos son mayores que 0")
# # any
# if any([x > 0, y > 0, z > 0]):
#     print(f"Al menos uno es positivo")
# %% 4. Bucles
# 1. For -->
# frutas = ['manzana', 'cereza', 'plátano']
# for fruta in frutas:
#     print(f"mi fruta es {fruta}")
# diccionario = {'d': 1, 'a': 3, 'Sebastian': 4}
# # for c in diccionario:
# #     print(f"la clave es {c}")
# # for valores in diccionario.values():
# #     print(f"los valores son {valores}")

# diccionario2 = {'Sebastian': {'Coche': {'Marca': 'Ferrari', 'kms': 100000}},
#                 'Javier': {'Coche': {'Marca': 'mercedes', 'kms': 200000}},
#                 'Manu': {'Coche': {'Marca': 'honda', 'kms': 300000}}
# }

# for clave in diccionario2:
#     print(f"El coche de {clave} es {diccionario2[clave]['Coche']}")
# for clave in diccionario:
#     print(f"la clave es {diccionario[clave]}")
# # for clave, valor in diccionario.items():
# #     print(f"La clave es {clave} y el valor es {valor}")
# for clave in diccionario2:
#     print(
#         f"los kms del coche de {clave} son {diccionario2[clave]['Coche']['kms']}")
# palabra = 'hOLA MUNDO'
# for letra in palabra:
#     print(letra)
# Intrucciones especiales --> Break, continue
# n = [1, 2, 3, 4, 5]
# for numero in n:
#     if numero == 4:
#         continue
#     print(numero)

# lista = [x for x in range(1, 6)]
# # print(lista)
# diccionario = {x: x**2 for x in range(1, 6)}
# nombres = ["Sebastian", "Javier", "Manu"]
# edades = [19, 19, 26]
# for n, e in zip(nombres, edades):
#     print(f"La edad de {n} es {e}")

# for i in range(11, 0, -2):
#     print(i)
# %% 5. Funciones en python


# def saludar(nombre = None):
#     if nombre is None:
#         nombre = 'amigo'
#         print(f"Hola {nombre}, no has introducido tu nombre")
#     return f"Hola, {nombre}"


# saludar()


# %% 6. Programación orientada a objeto (POO)

"""                         ¿Qué es una clase?
 Una clase es un molde o plantilla a partir de la cual se crean los objetos.
 La clase define un conjunto de atributos (características)
 y métodos (acciones (funciones)) que un objeto de esa clase puede tener.

 - Atributos: Son variables que almacenan datos relacionados con el objeto.
 - Métodos: Son funciones dentro de la clase que definen las acciones o
            comportamientos que puede realizar un objeto.

                           ¿Que es un objeto
 Un objeto es una instancia de una clase. Cuando se crea un objeto, se crea
 una entidad específica basada en la plantilla definida por la clase. Cada
 objeto tiene su propio conjunto de atributos (variables) y puede ejecutar
 los métodos definidos en la clase.
"""

"""
- __init__(self, ...): Este es el constructor que se ejecuta cuando se crea
 un nuevo objeto. Toma los parámetros marca, modelo y color y los asigna a
 los atributos del objeto.
"""


# import pandas as pd
# from pymongo import MongoClient
# import pymongo
# class Coche:

#     def __init__(self, marca, modelo, color, cv):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.cv = cv

#     def describir_coche(self):
#         return f"Mi coche es un {self.marca} {self.modelo} de color {self.color} con {self.cv} CV"

#     def caballos(self):
#         return f"El coche tiene {self.cv}"

#     def cambiar_color(self, n_color):
#         self.color = n_color


# mi_coche = Coche("Honda", "Civic", "azul", 140)
# mi_coche.cambiar_color("rojo")
# print(mi_coche.describir_coche())
# mi_coche.caballos()

"""                      Herencia y poliformismo
- La herencia es un concepto fundamental en POO que permite a una clase hija
heredar atributos y métodos de una clase padre. La herencia fomenta la
reutilización de código y permite extender las funcionalidades de las
clases existentes.

- El polimorfismo es la capacidad de que diferentes clases tengan
métodos con el mismo nombre, pero que se comporten de manera diferente.
El polimorfismo permite tratar objetos de diferentes clases de manera uniforme.
 """
# Herencia y poliformismo
# Clase padre --> Animal


# class Animal:

#     def __init__(self, nombre):
#         self.name = nombre

#     def hablar_init(self):
#         return f"{self.name} hace x sonido"


# class Perro(Animal):

#     def hablar(self):
#         return f"{self.name} hace Guau"

#     def raza(self, raza):
#         self.raza = raza
#         return f"La raza de {self.name} es {self.raza}"


# mi_perro = Animal("Indio")
# print(mi_perro.hablar_init())
# mi_perro2 = Perro("Indio")
# print(mi_perro2.raza("chucho"))
# print(mi_perro2.hablar())


"""                    Composicion de clases y agregación

- En la composición, un objeto contiene a otro objeto como parte esencial de
 sí mismo. Si el objeto contenedor deja de existir, el objeto contenido también
 deja de existir. Es una relación de tipo "parte de".
- En la agregación, un objeto contiene una referencia a otro objeto, pero no
 es responsable de su existencia. El objeto contenido puede existir
 independientemente del objeto contenedor. Es una relación de tipo "tiene un",
 pero no tan fuerte como la composición.
"""
# Composición


# class Tipo_Motor:

#     def __init__(self, CV):
#         self.motor = CV


# class Coche:

#     def __init__(self, marca, modelo, CV):
#         self.marca = marca
#         self.modelo = modelo
#         self.CV = Tipo_Motor(CV)

#     def detalles(self):
#         return f"Es un {self.marca} modelo {self.modelo} con {self.CV.motor} CV"


# Coche1 = Coche("Honda", "Civic", 140)
# print(Coche1.detalles())
# Agreagación

# class Profesor:

#     def __init__(self, nombre):
#         self.nombre = nombre


# class Instituto:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.profesores = []

#     def añadir_profesores(self, profesor):
#         self.profesores.append(profesor)

#     def mostrar_profesores(self):
#         for profesor in self.profesores:
#             print(profesor.nombre)


# # Se crea el instituto
# Instituto = Instituto("Las Salinas-Tarde")

# profe1 = Profesor("Dani")
# profe2 = Profesor("Vicente")
# profe3 = Profesor("Manu")

# Instituto.añadir_profesores(profe1)
# Instituto.añadir_profesores(profe2)
# Instituto.añadir_profesores(profe3)

# Instituto.mostrar_profesores()

"""                       Clases abstratas
En la Programación Orientada a Objetos (POO), las interfaces y clases
 abstractas son conceptos que permiten definir un contrato o plantilla de
 comportamiento para otras clases. A través de ellas, podemos asegurarnos de
 que ciertas clases implementen métodos específicos, aunque no sepamos
 exactamente cómo funcionarán esos métodos hasta que se implementen
 en clases concretas.
"""
# Clase padre


# from abc import ABC, abstractmethod
# class Animal(ABC):

#     @abstractmethod
#     def sonido(self):
#         pass  # pasa al método de cada clase hija

#     def come(self):
#         return f"El animal esta comiendo"
# # Clases hijas


# class Perro(Animal):

#     def sonido(self):
#         return "Guau!"


# class Gato(Animal):

#     def Saltar(self):
#         return f"El gato salta"

#     def Sonido(self):
#         return f"El gato hace Miau!"


# perro = Perro()
# Gato = Gato()
# print(perro.sonido())
# print(Gato.sonido())

# Variables globales y locales
# x = 'global'


# def ejemplo():
#     x = 'local'
#     print(x)


# ejemplo()
# print(x)

# Modificar variable global
# x = 'Global'


# def cambiar_var_global():
#     global x
#     x = 'Global_modificada'
#     print(x)


# cambiar_var_global()
# print(x)


# def externa():
#     x = 'Externa'

#     def interna():
#         nonlocal x
#         x = 'Externa_modificada'
#         print(x)

#     interna()


# externa()

# %% 7. extraer y pedir información de ficheros, tratarla y devolverla
# 1. Extraer y tratarla
# Modulo pandas --> Leer, tratar, escribir, etc.
# Leer
# import pandas as pd
# archivo = pd.read_csv('empleados.csv')
# Extraer información
# print("Los datos de los empleados son:", archivo)
# Acceder a columnas
# nombres = archivo['nombre']
# print("Los nombres son", nombres)
# # Acceder a filas
# primer_empleado = archivo.loc[0]
# # Acceder a un valor en concreto
# salario_3 = archivo.loc[2, 'salario_mensual']
# # 2. Pedir información por pantalla y cargarla
# nueva_fila = {
#     'nombre': 'Javier',
#     'edad': 19,
#     'id_emp': 105,
#     'horas_trabajadas': 20,
#     'tarifa_hora': 20,
#     'salario_mensual': None
# }
# # Añadir --> append
# nueva_fila2 = pd.DataFrame([nueva_fila])
# archivo = pd.concat([archivo, nueva_fila2])
# Cargar información

# Tk().withdraw()

# Pedimos al usuario que seleccione el archivo .csv

# from tkinter import Tk
# import pandas as pd
# from tkinter.filedialog import askopenfilename
# file_path = askopenfilename(
#     title='Selecciona un archivo .csv',
#     filetypes=[("CSV files", "*.csv")])

# if file_path:
#     # Leer
#     df = pd.read_csv(file_path)


# else:
#     print("No has seleccionado ningún archivo")


# 3. Crear un archivo y grabarlo
# Inicializar Tkinter
# from tkinter import Tk, Toplevel
# import pandas as pd
# from tkinter.filedialog import askdirectory
# import os
# root = Tk()
# root.withdraw()  # Ocultamos la ventana principal de Tkinter
# # Crear una ventana temporal solo para ser usada como base del diálogo
# ventana_temporal = Toplevel()
# ventana_temporal.withdraw()
# ventana_temporal.attributes('-topmost', True)
# # Creamos el archivo que queremos escribir
# data = {
#     'nombre': ['Sebastian', 'Javier', 'Manu', 'Iván'],
#     'edad': [19, 19, 26, 20],
#     'Salario': [None, 1650, 1799, 4000]}
# # Convertimos el archivo a dataframe
# df = pd.DataFrame(data)
# # seleccionar carpeta y nombre archivo
# carpeta_select = askdirectory(
#     title='Selecciona directorio', parent=ventana_temporal)
# nombre_archivo = 'Empleados2.csv'
# # Verificar selección y guardar con os
# if carpeta_select:
#     file_path = os.path.join(
#         carpeta_select, nombre_archivo)  # Se contruye la ruta
#     # guardamos dataframe
#     df.to_csv(file_path, index=False)
#     print(f"Archivo guardado en: {file_path}")
#     print(df)
# else:
#     print("No has seleccionado ninguna carpeta")

# # Cerrar la ventana temporal y finalizar Tkinter
# ventana_temporal.destroy()
# root.quit()
# %% 8. Conexión a base de datos.
""" Relacionales --> MYSQL/PostgreSQL"""
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
# # Función para conectarnos
# def connec_BD(host, database, user, password, port):
#     try: 
#         connection = mysql.connector.connect(
#             host=host,
#             database=database,
#             user=user,
#             password=password,
#             port=port)
#         if connection.is_connected():
#             print(f"La conexión ha sido existosa {database}")
#             return connection
#     except Error as e:
#             print(f"Erro al conectarse: {e}")
#             return None
# # Función para leer la BD
# def read_DB(connection, tabla, columnas, limite_filas):
#     try: 
#         cursor = connection.cursor()
#         # Petición
#         columnas_str = ','.join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
#         # Ejucutamos la petición
#         cursor.execute(query)
#         # Resultados
#         resultados = cursor.fetchall()
#         # Obtener 
#         columnas_resultado = [i[0] for i in cursor.description]
#         # Nos creamos el dataframe
#         df = pd.DataFrame(resultados, columns=columnas_resultado)
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
#         return None
    
# # Ejecutar
# if __name__ == '__main__':
#     # Parámetros de conexión
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = ''  # No requiere contraseña
#     port = 4497
#     # Parámetros de la consulta 
#     tabla = 'family'  # Tabla a consultar
#     # Columnas que quieres extraer
#     columnas = ['rfam_acc', 'rfam_id', 'description']
#     limite_filas = 5  # Número de filas que quieres extraer                         
#     # Conectar a la BD
#     conexion = connec_BD(host, database, user, password, port)
#     if conexion:
#         # Leer
#         df_BD = read_DB(conexion, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()


# Conectar a la base de datos pública de Rfam
# Importar módulos relacionados
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
# # 1. Conexión a la BBDD
# def conectar_BBDD(host, database, user, password, port):
#     try:
#         connection = mysql.connector.connect(
#             host=host,
#             database=database,
#             user=user,
#             password=password,
#             port=port
#         )
#         if connection.is_connected():
#             print(f"Conexión exitosa a la base de datos {database}")
#             # Obtener información de la base de datos
#             cursor = connection.cursor()
#             cursor.execute("SELECT DATABASE();")
#             cursor.fetchone()  # Asegurarse de consumir el resultado
#             return connection
#     except Error as e:
#         print(f"Error al conectar a la base de datos: {e}")
#         return None
# # 2. Leer datos de la tabla especificada y con las columnas deseadas
# def leer_BBDD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         # Convertir la lista de columnas en una cadena separada por comas
#         columnas_str = ', '.join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
#         # Ejecutar la consulta
#         cursor.execute(query)
#         resultados = cursor.fetchall()
#         # Obtener nombres de columnas del cursor
#         columnas_resultado = [i[0] for i in cursor.description]
#         # Convertir resultados a DataFrame
#         df = pd.DataFrame(resultados, columns=columnas_resultado)
#         return df
#     except Error as e:
#         print(f"Error al leer datos: {e}")
#         return None
# # 3. Ejecución
# if __name__ == "__main__":
#     # Parámetros de la conexión
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = ''  # No requiere contraseña
#     port = 4497
#     # Parámetros de la consulta (puedes modificarlos según tus necesidades)
#     tabla = 'family'  # Tabla a consultar
#     # Columnas que quieres extraer
#     columnas = ['rfam_acc', 'rfam_id', 'description']
#     limite_filas = 5  # Número de filas que quieres extraer
#     # Conectar a la base de datos
#     conexion = conectar_BBDD(host, database, user, password, port)
#     if conexion:
#         # Leer la tabla especificada
#         df_familias = leer_BBDD(conexion, tabla, columnas, limite_filas)
#         if df_familias is not None:
#             print(df_familias)
#         conexion.close()

""" No relacionales --> MONGODB"""
# # Importar módulos
# import pymongo
# import pandas as pd
# # Conexión
# try: 
#     cliente = pymongo.MongoClient(
#         "mongodb+srv://manuel10benito:x6HWnCibWBsVpi9v@cluster0.sq23v.mongodb.net/?retryWrites=true&w=majority")
#     print("Conexión exitosa")
# except Exception as e:
#     print(f"Error en la conexión {e}")
#     exit()
# # Extraer información
# db = cliente["sample_mflix"]
# coleccion = db["movies"]
# # Hacer la consulta
# try:
#     resultados = coleccion.find().limit(10)
#     lista_resultados = list(resultados)
#     # Verificar si se han extraido los resultados
#     if not lista_resultados:
#         print("No se han encontrado datos")
#     else:
#         print(f"Se han encontrado {len(lista_resultados)} documentos")
#         df = pd.DataFrame(lista_resultados)
# except Exception as e:
#     print(f"Error al realizar la consulta: {e}")

# Lista --> Dataframe

        




















# CONECTARNOS A MONGO DB--> Peticion: "mongodb+srv://manuel10benito:x6HWnCibWBsVpi9v@cluster0.sq23v.mongodb.net/?retryWrites=true&w=majority"
# import pymongo  # Para conectarse a MongoDB
# import pandas as pd  # Para manipular los datos como DataFrames

# try:
#     client = pymongo.MongoClient(
#         "mongodb+srv://manuel10benito:x6HWnCibWBsVpi9v@cluster0.sq23v.mongodb.net/?retryWrites=true&w=majority"
#     )
#     print("Conexión exitosa a MongoDB Atlas.")
# except Exception as e:
#     print(f"Error en la conexión: {e}")
#     exit()  # Salir si hay un problema de conexión

# # Acceder a la base de datos y colección específicas
# db = client["sample_mflix"]
# collection = db["movies"]
# # Hacer una consulta a la colección
# try:
#     resultados = collection.find().limit(5)
#     lista_resultados = list(resultados)

#     # Verificar si se encontraron resultados
#     if not lista_resultados:
#         print("No se han encontrado documentos en la colección.")
#     else:
#         print(f"Se han encontrado {len(lista_resultados)} documentos.")
# except Exception as e:
#     print(f"Error al realizar la consulta: {e}")

# # Convertir los resultados a un DataFrame para mejor visualización
# try:
#     df = pd.DataFrame(lista_resultados)
#     print("Datos convertidos a DataFrame.")
#     print(df.head())  # Mostrar los primeros datos del DataFrame
# except Exception as e:
#     print(f"Error al convertir a DataFrame: {e}")
# %% 9. Consumo y creación de APIs
# Consumo de APIs
# import requests
# # url
# url = "https://pokeapi.co/api/v2/pokemon?limit=150"
# # Respuesta
# respuesta = requests.get(url)

# lista_pokemon = respuesta.json()["results"]

# for pokemon in lista_pokemon:
#     print(pokemon["name"])

# PVGIS

# Definir la URL de la API de PVGIS y los parámetros para la consulta
import json
import requests
base_url = "https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"

# Parámetros de la solicitud (Madrid, España)
params = {
    'lat': 40.4168,  # Latitud 
    'lon': -3.7038,  # Longitud 
    'peakpower': 1,  # Potencia pico del sistema (kW)
    'pvtechchoice': 'crystSi',  # Tipo de tecnología PV (Silicio cristalino)
    'loss': 14,  # Pérdidas del sistema (%)
    'outputformat': 'json'  # Formato de salida
}

# Realizar la solicitud GET
response = requests.get(base_url, params=params)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Cargar el contenido JSON en una variable de Python
    data = json.loads(response.text)
    
    # Mostrar parte de la información
    print("Datos obtenidos de PVGIS:")
    print(f"Energía diaria estimada: {data['outputs']['totals']['fixed']['E_d']} kWh")
    print(f"Energía anual estimada: {data['outputs']['totals']['fixed']['E_y']} kWh")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")


# Creación de APIs
# Crear la API
from flask import Flask, jsonify

app = Flask(__name__)

# Ruta principal con respuesta en formato JSON
@app.route('/api', methods=['GET'])
def obtener_datos():
    # Datos en formato JSON
    datos = {
        "nombre": "Javi",
        "edad": 19,
        "ciudad": "Seseña"
    }
    return jsonify(datos)

# Ruta para obtener una lista de datos
@app.route('/api/lista', methods=['GET'])
def obtener_lista():
    lista_datos = [
        {"nombre": "Sebastián", "edad": 19, "ciudad": "Seseña"},
        {"nombre": "Javier", "edad": 19, "ciudad": "Seseña"},
        {"nombre": "Manu", "edad": 26, "ciudad": "Illescas"}
    ]
    return jsonify(lista_datos)

if __name__ == '__main__':
    app.run(debug=True)
    
# Alojar API en un servidor




# %% 10. Módulos más comunes
# """ 1. Math: El módulo math proporciona acceso a funciones matemáticas comunes,
#  como trigonometría, logaritmos, factoriales, etc."""
# import math
# # Raíz cuadrada
# print(math.sqrt(16))  
# # Logaritmo natural
# print(math.log(2.7183)) 
# # Valor de Pi
# print(math.pi)  
# """ 2. El módulo random es útil para generar números aleatorios, simular
#  lanzamientos de monedas, dados,etc."""
# import random
# # Número aleatorio entre 0 y 1
# print(random.random())
# # Número entero aleatorio entre 1 y 10
# print(random.randint(1, 10))
# # Selección aleatoria de una lista
# frutas = ['manzana', 'banana', 'naranja']
# print(random.choice(frutas))
# """ 3. datetime: El módulo datetime permite trabajar con fechas, horas,
#  intervalos de tiempo y realizar cálculos relacionados con el tiempo."""
# from datetime import datetime
# # Fecha y hora actuales
# ahora = datetime.now()
# print(ahora)
# # Formatear la fecha
# fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
# print(fecha_formateada)
# # Calcular diferencia entre fechas
# fecha1 = datetime(2023, 1, 1)
# fecha2 = datetime(2024, 1, 1)
# diferencia = fecha2 - fecha1
# print(f"Días de diferencia: {diferencia.days}")
# fin = datetime.now()
# tiempo_ejecucion = fin - ahora
# print(f"El tiempo de ejecución ha sido de {tiempo_ejecucion} segundos")
# """ 4. Matplot. matplotlib es la biblioteca más usada para hacer gráficos en
#  Python. Es ideal para generar gráficos de líneas, barras, histogramas, entre
#  otros."""
# import matplotlib.pyplot as plt
# # Datos
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# # Crear un gráfico de línea
# plt.plot(x, y, label="Crecimiento")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Gráfico de línea simple')
# plt.legend()
# plt.show()
# """ 5. seaborn: Visualización avanzada
# seaborn se utiliza para crear visualizaciones más avanzadas,
#  como gráficos de distribución, correlaciones, etc."""
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# # Crear un DataFrame con datos de ejemplo
# df = pd.DataFrame({
#     'edad': [25, 30, 35, 40, 45],
#     'salario': [40000, 50000, 60000, 70000, 80000]
# })
# # Crear un gráfico de dispersión
# sns.scatterplot(x='edad', y='salario', data=df)
# plt.show()
# %%. 11. Utilización de Github para seguimiento y actualización de proyectos