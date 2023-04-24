# ERRORES Y EXCEPCIONES

# El error indica un problema de tipo no contrololado. 
# Sin embargo, las excepciones, son los problemas/errores
# que a priori deberían poder ser controlados.

# En python sueles ocurrir mayoritariamente dos tipos de errores
# y según cómo los tratemos, estos errores los podemos convertir
# es excepciones:

#   1 . Errores de sintaxis
#   2 . Errores en tiempos de ejecución
#   3 . Errores lógicos

"""
ERRORES DE SINTAXIS

1. Omitir una palabra clave
2. Colocar una palabra clave en el lugar equivocado
3. Omitir un símbolo, como los dos puntos, la coma o los corchetes
4. Escribir mal una palbra clave
5. Añadir una sangría incorrecta
6. Dejar un bloque vacío

"""

a = 8
if a > 8:
# el siguiente print() debería ir indentado
print("a es mayor que 8")

"""
Salida:

File "<ipython-input-2-b10368b60067>", line 29
    print("a es mayor que 8)
    ^ 
IndentationError: expected an indented block

"""


"""
ERRRORES EN TIEMPO DE EJECUCIÓN

1. División por cero
2. Realizar una operación sobre tipos de datos incompatibles
3. Utilizar un identificador que no ha sido definido
4. Intentar acceder a un elemento de lista, archivo, diccionario o atributo de objeto que no existe

"""


"""
ERRORES LÓGICOS

1. Utilizar un nombre de variable incorrecto
2. Utilizar la división de enteros en lugar de la división en coma flotante
3. Equivocarse en la priorización de los operadores

"""


"""
EXCEPCIONES

"""

# Esta linea de código nos da un Error de Excepción dado que tenemos
# una división por cero

print(10/0)

"""
ZeroDivisionError: division by zero
"""


"""
ELEVAR UNA EXCEPCIÓN (CREARLA NOSOTROS MISMOS)
Podemos crear excepciones mediante raise
"""

z = 20
if z > 15:
    raise Exception("z no puede exceder el valor 15 y su valor era: {}".format(z))


"""
AFIRMACIÓN
"""

import sys
assert ("linux" in sys.platform), "Este código sólo puede ejecutarse en Linux"
print("No renuncies a tus sueños... Sigue durmiendo")

"""
AssetionError: Este código sólo puede ejecutarse en Linux
"""


"""
MANEJO
try y except se utiliza para atrapar y manejar excepciones
"""

def division(x, y):
    z = x / y
    return z

try:
    resultado = division(10/0)
    print(resultado)
except ZeroDivisionError:
    print("¡Estás tratando de hacer una división entre cero!")
print("No renuncies a tus sueños... Sigue durmiendo")

division(10/0)


"""
try:
    Ejecución normal del bloque
except A:
    Excepción A
except B:
    Excepción B
except:
    Otro tipo de excepción
else:
    Si no es una excepción llega aquí
finally:
    final
"""
