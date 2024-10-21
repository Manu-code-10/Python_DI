# %% CABECERA
"""
Fecha: 04/10/2024.
Profesor: Manuel Benito.
Asignatura: Diseño de Interfaces (DI).
"""
import numpy as np
# %% 1. Hola mundo (mostrar información por consola).
print("Hola mundo")

# %% 2. Pedir información por consola.
nombre = input("¿Cual es tu nombre? ")
""" Como se puede ver no se ha tenido que especificar el
    tipo de variable....."""
edad = input("¿Cúantos años tienes? ")
print("Hola", nombre, "Tienes", edad)

# %% 3 Cuidado con las variables.
# Para hacer ver que si hay que decir el tipo de variable. Es lo mejor siempre
# ¡input siempre guarda la variable como tipo string!
edad = int(input("¿Cúantos años tienes? "))
if edad > 25:
    print("Hola", nombre, "tienes", edad,
          "años, lo que significa que eres un poco viejo ya...")
else:
    print("Hola", nombre, "tienes", edad,
          "años, lo que significa que eres joven todavia...")

# %% 4. Manejo de errores
nombre = input("¿Cual es tu nombre? ")
# Verificar si la primera entrada es de tipo string
if nombre.isdigit():
    print("Error: El nombre no debe ser un número.")
    exit()
# Verificar si la segunda entrada es un número
try:
    edad = int(input("¿Cuántos años tienes? "))
except ValueError:
    print("Error: La edad debe ser un número.")
    exit()
""" Hay muchos más formas... buscar información y emplear el mejor para cada caso"""
# %% 5. Tipos de variables
# 5.1 Inmodificables (que no se pueden modificar una vez creados)
"""
Estos tipos de datos son: Enteros(int), cadenas de texto (str), tuplas(tuple),
                          float y bool.
"""
a = 10
b = 10
print(id(a), id(b))  # Muestra el mismo ID, indicando que apuntan al mismo objeto
# 5.1.1 Enteros
a = 5
b = a
a = 10
print(a, b)  # a = 10, b = 5
"""
Cuando asignas b = a, ambos apuntan al mismo valor (5). 
Sin embargo, al modificar a y asignarle 10, 
se crea un nuevo entero en memoria y a apunta a ese nuevo objeto. b sigue apuntando al valor original (5).
"""
# 5.1.2 str
"""
Las cadenas en Python son inmutables. Cualquier operación que "modifique" una cadena en realidad crea una nueva cadena.
"""
# 5.1.3 Tuplas
"""
Las tuplas son como listas inmutables: una vez que se crean, 
sus elementos no pueden ser modificados.
Pueden tener elementos de diferentes tipos. Acceso por índice, EMPIEZA EN 0.
Las tuplas se utilizan en varias situaciones donde es útil 
tener una secuencia de elementos que no debe cambiar. 
Mejor rendimiento.
Uso como clave en diccionarios.
"""
tupla = (1, 2, 3)
# Esto generará un error: TypeError: 'tuple' object does not support item assignment
tupla[0] = 10
nueva_tupla = tupla + (4,)
print("La tupla inicial es:", tupla)        # (1, 2, 3)
print("La nueva tupla es:", nueva_tupla)  # (1, 2, 3, 4)
# USO TUPLAS
# funciones


def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta


resultado = calcular(10, 5)
print(type(resultado))  # Imprime (15, 5)
# asignar valores
a, b, c = (1, 2, 3)
print(a, b, c)  # Imprime 1 2 3
#
# 5.2 Modificables (que se pueden modificar una vez creados)
"""
Estos tipos de datos son: Listas (list), diccionarios (dict), conjuntos (set),
"""
# 5.2.1 Listas
"""
- Las listas son vectores dinámicos, es decir, 
se puede cambiar su contenidos y sigue
siendo el mismo en memoria. Se crean con corchetes.
- Igual que con las tuplas, puedes acceder
 a los elementos de una lista mediante su índice, que comienza desde 0.
- Las listas pueden contener otras listas como elementos, 
permitiendo la creación de estructuras de datos multidimensionales.
"""
# creacion de listas
lista = [10, 20, 30]
print(lista[0])
# Listas anidadas
lista_anidada = [1, 2, [3, 4, [5, 6]]]
print(lista_anidada[2][2][0])  # Imprime 5
# append
lista.append(4)
print(lista)
# extend
lista.extend([4, 5, 6])
print(lista)
# insert
lista.insert(1, "a")
print(lista)
# remove
lista.remove(2)
print(lista)
# pop
elemento = lista.pop()  # Elimina y devuelve el último elemento
print(lista)
print(elemento)  # Salida: 4
elemento = lista.pop(1)  # Elimina el elemento en el índice 1 (2)
print(lista)
print(elemento)  # Salida: 2
# sort
lista.sort()
print(lista)
lista.sort(reverse=True)
# suma
total = sum(lista)
print(total)
#################################################
# ITERAR SOBRE LISTAS
mi_lista = [1, 2, 3, 4]
for elemento in mi_lista:
    print(elemento)  # Imprime cada elemento de la lista en una nueva línea
    ######################################################################
    ## Ejercicio clase ##
# A pelo
Matriz1 = []
n_filas1 = 2  # dimension de filas 1
n_columnas1 = 2   # dimensión de columas 1
n_filas2 = 2  # dimension de filas 2
n_columnas2 = 2  # dimensión de columas 2
n_filas3 = 4  # dimension de filas 3
n_columnas3 = 3  # dimensión de columas 3
c1 = 1  # es un contador
# Bucle matriz
for i in range(n_filas1):
    filai1 = []
    for j in range(n_columnas1):
        filai1.append(c1)  # Se guarda el valor en la fila
        c1 += 1  # Se actualiza el contador
    Matriz1.append(filai1)  # Se carga en la lista el resultado

# Matriz dentro de matriz más sencillo
M = [[0 for _ in range(n_columnas1)]
     for _ in range(n_filas1)]  # Se inicializa la Matriz
for i in range(n_filas1):
    for j in range(n_columnas1):
        M[i][j] = [[0 for _ in range(n_columnas2)]
                   for _ in range(n_filas2)]
        c2 = 1
        for ii in range(n_filas2):
            for jj in range(n_columnas2):
                M[i][j][ii][jj] = c2
                c2 += 1

print(M[1][1][1][0])  # Estamos en el elemento 2,2 de la matriz principal

# Matriz dentro de matriz dentro de matriz
M2 = [[0 for _ in range(n_columnas1)]
      for _ in range(n_filas1)]  # Se inicializa la Matriz
for i in range(n_filas1):
    for j in range(n_columnas1):
        M2[i][j] = [[0 for _ in range(n_columnas2)]
                    for _ in range(n_filas2)]

        for ii in range(n_filas2):
            for jj in range(n_columnas2):
                M2[i][j][ii][jj] = [[0 for _ in range(n_columnas3)]
                                    for _ in range(n_filas3)]
                c3 = 1
                for iii in range(n_filas3):
                    for jjj in range(n_columnas3):
                        M2[i][j][ii][jj][iii][jjj] = c3
                        c3 += 1

print(M2[1][1][1][0][1][0])  # Estamos en el elemento 2,2

# Libreria Numpy
Matriz2d = np.arange(1, n_filas1 * n_columnas1 + 1)
Matriz2d = np.reshape(Matriz2d, (n_filas1, n_columnas1))
# Crear una matriz multidimensional con NumPy
# El tamaño total será n_filas1 x n_columnas1 x n_filas2 x n_columnas2 x n_filas3 x n_columnas3
M3 = np.arange(1, n_filas1 * n_columnas1 * n_filas2 * n_columnas2 * n_filas3 * n_columnas3 + 1).reshape(
    n_filas1, n_columnas1, n_filas2, n_columnas2, n_filas3, n_columnas3)
# OJO CON LOS MODIFICLABLES
"""
Los objetos mutables, como listas y diccionarios, 
requieren más cuidado en cuanto a referencias. 
Si asignas una lista a una nueva variable, 
ambas variables apuntarán al mismo objeto en memoria.
"""
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # [1, 2, 3, 4] (ambas variables apuntan al mismo objeto)
# 5.2.2 Diccionarios
"""
Un diccionario es una estructura de datos en Python que almacena pares
 de clave-valor. Cada clave es única y se utiliza para acceder
 a su valor correspondiente. Los diccionarios permiten un acceso
 rápido a los datos basándose en la clave y son muy útiles cuando
 se necesita almacenar datos relacionados de forma que se pueda buscar
 fácilmente mediante una clave en lugar de un índice.
"""
# sintaxis
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
# acceso por clave y únicas
print(diccionario["nombre"])  # Salida: Juan
print(diccionario["edad"])    # Salida: 25
# son modificables
diccionario["edad"] = 26  # Modificar el valor de una clave
diccionario["pais"] = "España"  # Agregar un nuevo par clave-valor
print(diccionario)
# Podemos tener diferentes tipos dentro de un diccionario
estudiante = {"nombre": "Carlos", "edad": 22,
              "cursos": ["Matemáticas", "Física"]}
# ES UNA BASE DE DATOS
empleados = {
    "empleado1": {"nombre": "Ana", "puesto": "Ingeniera", "salario": 35000},
    "empleado2": {"nombre": "Luis", "puesto": "Analista", "salario": 30000}
}
# FUNCIONES ESPECIFICAS
# KEYS
claves = diccionario.keys()
print(claves)
# VALUES
valores = diccionario.values()
print(valores)
# ITEMS--> dEVUELVE TUPLAS SEPARADAS
items = diccionario.items()
print(items)
# COGER VALORES ESPECÍFICOS
edad = diccionario.get("edad")
pais = diccionario.get("pais")
print(edad)   # Salida: 25
print(pais)   # Salida: Desconocido
# POP --> BORRAR
edad = diccionario.pop("edad")
print(edad)        # Salida: 25
print(diccionario)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid'}
# UPDATE --> aCTUALIZAR EL DICCIONARIO ACTUAL CON OTRO
diccionario = {"nombre": "Juan", "edad": 25}
nuevo_diccionario = {"ciudad": "Madrid", "pais": "España"}
diccionario.update(nuevo_diccionario)
print(diccionario)
# 5.2.3 CONJUNTOS
"""
Un conjunto es una colección no ordenada de elementos únicos.
 A diferencia de las listas y las tuplas, los conjuntos no permiten elementos duplicados,
 y no mantienen el orden de los elementos.
 - ¿Para qué se utilizan?
Eliminar duplicados: Los conjuntos son útiles cuando necesitas eliminar elementos
 duplicados de una lista o verificar la unicidad de los datos.
 
Operaciones matemáticas: Puedes realizar operaciones de teoría de conjuntos 
como intersección, unión, diferencia y diferencia simétrica.
"""
mi_conjunto = {1, 2, 3, 4, 4, 5}
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5}

# Operaciones comunes
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
print(conjunto1.union(conjunto2))      # Unión: {1, 2, 3, 4, 5}
print(conjunto1.intersection(conjunto2))  # Intersección: {3}
print(conjunto1.difference(conjunto2))  # Diferencia: {1, 2}

# OTROS TIPOS DE DATOS
# bOOOLEANOS
es_mayor = 5 > 3
print(es_mayor)  # Salida: True

if es_mayor:
    print("5 es mayor que 3")  # Salida: "5 es mayor que 3"
# Float
"""
Se utilizan cuando es necesario realizar operaciones con números no enteros,
 como cálculos financieros, científicos o cualquier situación que requiera precisión decimal.
"""
pi = 3.14159
radio = 5.5
area = pi * radio**2
print(area)  # Salida: 95.0331775
# compleejos
"""
El tipo complex representa números complejos en Python, 
los cuales tienen una parte real y una parte imaginaria.

¿Para qué se utilizan?
Útiles en matemáticas avanzadas, como álgebra y física,
 donde los números complejos se utilizan para resolver ecuaciones.
"""
numero_complejo = 3 + 4j
print(numero_complejo.real)  # Salida: 3.0 (parte real)
print(numero_complejo.imag)  # Salida: 4.0 (parte imaginaria)
# range
"""
¿Qué es?
range() genera una secuencia de números y se utiliza comúnmente en bucles for.
 Es un tipo de objeto especial que genera los valores sobre la marcha,
 por lo que es muy eficiente en términos de memoria.

¿Para qué se utiliza?
Iteración en bucles: Es la forma más común de iterar un número específico de veces.
"""
for i in range(5):
    print(i)  # Salida: 0, 1, 2, 3, 4
# bytes y bytearrays
"""
¿Qué son?
Bytes: Es una secuencia inmutable de enteros en el rango 0-255.
Bytearray: Similar a bytes, pero es mutable.
¿Para qué se utilizan?
Trabajar con datos binarios, como cuando se manejan archivos o se realizan 
operaciones de red, ya que estos tipos permiten un control preciso sobre la
 manipulación de bytes.
"""
datos = b'Hola'
print(datos[0])  # Salida: 72 (valor ASCII de 'H')

mutable_datos = bytearray(b'Hola')
mutable_datos[0] = 74  # Cambia 'H' por 'J'
print(mutable_datos)  # Salida: bytearray(b'Jola')

# %% 6. Alcance de variables//local, global.
"""
Las variables en Python tienen alcances o ámbitos que determinan dónde
 pueden ser accedidas o modificadas dentro de un programa. 
 Este es un concepto fundamental para entender cómo se
 comportan las variables dentro de funciones y fuera de ellas.
 
GLOBAL:Una variable global es aquella que se define fuera de cualquier 
función o bloque de código, por lo que está disponible para ser
 utilizada en cualquier parte del programa. Todas las funciones
 tienen acceso a las variables globales, pero no pueden modificarlas
 directamente a menos que se utilice la palabra clave global. 

lOCAL: Una variable local es aquella que se define dentro de una
 función o bloque de código, y su alcance está limitado
 a esa función. Una vez que se sale del bloque o función,
 la variable local deja de existir, es decir, solo
 es accesible dentro de la función donde se definió.
"""
x = "global"


def ejemplo():
    x = "local"
    print(x)  # Imprime "local"


ejemplo()
print(x)  # Imprime "global"

# SI NECESITAMOS MODIFICAR UNA VARIABLE GLOBAL
x = "global"  # Variable global


def cambiar_global():
    global x  # Indica que se modificará la variable global
    x = "modificada global"
    print(x)  # Imprime "modificada global"


cambiar_global()  # Cambia el valor de la variable global
print(x)  # Imprime "modificada global"

# Anidación de funciones y variables no locales (nonlocal)
"""
Cuando trabajas con funciones anidadas, puedes usar 
la palabra clave nonlocal para modificar una variable
 en un ámbito superior que no sea el global.

"""


def externa():
    x = "externa"  # Variable de la función externa

    def interna():
        nonlocal x  # Indica que se modificará la variable de la función externa
        x = "modificada en interna"
        print(x)  # Imprime "modificada en interna"

    interna()
    print(x)  # Imprime "modificada en interna"


externa()
"""
EXPLICACION: 
    nonlocal x: Modifica la variable x que pertenece a la función externa(),
    pero no toca ninguna variable global.
Después de llamar a la función interna(), 
la variable x en externa() también se ha modificado.
"""
# %% 7. Formato de cadenas

# %% 8. Sacar información de variables.

# %% 9. Conversión entre tipos

# %% 10.Funciones importantes

# %% 11. Introducción a las funciones lambda
