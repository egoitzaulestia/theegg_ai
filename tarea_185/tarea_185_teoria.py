"""
TRABAJAR CON FICHEROS

Algunos de los poderes que necesitarás en este ámbito para ser un digno científico de datos

 1. Recuperar las propiedades de los archivos
 2. Leer y escribir ficheros
 3. Comparar patrones de los archivos
 4. Recorrer árboles de directorios
 5. Crear directiorios y ficheros
 6. Crear archivos y directorios temporales
 7. Copiar, mover o renombrar archivos y directorios
 8. Eliminar archivos y directorios
 9. Crear y extraer archivos ZIP y TAR
10. ...

"""

# EJEMPLOS:

###############
# with open() #
###############

# Crear fichero y escribir con perminsos de escritura (w)
with open("hola.txt", "w") as doc:
    info = "Si el mundo es un pañuelo, ¿nosotros qué somos?"
# Escribir en el fichero
    doc.write(info)

# Permisos de lectura
with open("hola.txt", "r") as doc:
    print(doc.read())

"""
Salida:

Si el mundo es un pañuelo, ¿nosotros qué somos?
"""


##############
# módulos os #
##############

import os

# Ruta del directorio que queremos listar
ruta = "/Users/egoitzaulestiapadilla/01_CODE/00_AI/00_TheEgg" 
with os.scandir(ruta) as listas:
    for lista in listas:
        if lista.is_file():
            print(lista.name)

"""
Salida:

.DS_Store
hola.txt
superficieCuadrado.py
variable_local_global.py
"""

# Podemos listar los subdirectorios de un directorio
# Ruta del dirctorio cuyos subdirectorios que queremos listar
ruta = "/Users/egoitzaulestiapadilla/01_CODE/00_AI/00_TheEgg"
for lista in os.listdir(ruta):
    if os.path.isdir(os.path.join(ruta, lista)):
        print(lista)

"""
Salida:

tarea_180
tarea_186
tarea_181
tarea_182
tarea_185
"""

# Crear directorios con el clásico mkdir
# os.mkdir("exmple_directory")


###################
# Librería Pandas #
###################

import pandas as pd

# Indicar la ruta del csv que queremos leer
datos = pd.read_csv("/Users/egoitzaulestiapadilla/01_CODE/00_AI/00_TheEgg/tarea_185/mission_launches.csv")
# Listar primeras 3 filas
datos.head()
