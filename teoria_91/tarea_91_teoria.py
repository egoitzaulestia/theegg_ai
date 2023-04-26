# CONVENCIONES DE PTROGRAMACIÓN EN PYHTON Y EL PEP 8

# Tamaño máximo de líneas:
# ---------------------------------------------------
# Máximo 79 lineas


# Líneas en blanco:
# - Separar clases y funciones mediante 2 líneas en blanco
# - Los métodos dentro de las clases se separan con una línea
# - Separar partes del código que realizan tareas distintas por una línea en blanco


# Imports:
# ---------------------------------------------------
# Los distintos imports deben de estar en distintas lineas
import os
import sys

# NO: import os, sys

# Sí se puede...
from subprocess import Popen, PIPE

a = 1
b = 2

a + b # SÍ
a+b   # NO
