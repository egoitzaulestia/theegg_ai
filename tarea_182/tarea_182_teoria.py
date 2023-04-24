"""
EXPRESIONES REGULARES CON PYTHON

"""

# Importamos librería
import re

cadena = "Odio que hablen cuando interrunpo"

# Buscar palabra "hablen". r significa que toma en cuenta la cadena en bruto.
buscar = re.search(r"hablen", cadena)

# Posición de cominzo y de final
print("Hablen empeiza en la posición:", buscar.start())
print("Hablen finaliza en la posición:", buscar.end())

"""
Salida:
Hablen empeiza en la posición: 9
Hablen finaliza en la posición: 15
"""


# Casos de uso:

# BARRA INVERTIDA (\)

cadena = "Voy hacer dieta. Oh, ¡mira! ¡Una hamburguesa!"

# sin \
rtdo = re.search(r".", cadena)
print(rtdo)

# con \
rtdo = re.search(r"\.", cadena)
print(rtdo)

"""
Salida:
<re.Match object; span=(0, 1), match='V'>
<re.Match object; span=(15, 16), match='.'>
"""


# LOS CORCHETES []

cadena = "Voy hacer dieta. Oh, ¡mira! ¡Una hamburguesa!"

rtdo = re.search(r"^Voi", cadena)
print(rtdo)

"""
Salida:
None
"""

cadena = "Voy hacer dieta. Oh, ¡mira! ¡Una hamburguesa!"

rtdo = re.search(r"hamburguesa!$", cadena)
print(rtdo)

"""
Salida:
<re.Match object; span=(33, 45), match='hamburguesa!'>
"""


# Un clásico: VALIDADOR DE CORREOS

# regex
expresion_regular = "^[a-z0-9]+[\._]?[@]\w+[.]\w{2,3}$"

def validar(email):
    if (re.search(expresion_regular, email)):
        print("Email válido")
    else:
        print("Email no válido")

validar("hola@theegg.ai")

"""
Salida:
Email válido
"""
