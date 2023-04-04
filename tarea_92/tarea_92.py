# TIPOS DE LIBRERÍAS

# 1. Visualizacion
# 2. Cálculo Numérico
# 3. Machine Learning
# 4. Deep Learning
# 5. Procesamiento de Lenguaje Natural
# 6. Y más...

# Algunas delas librerías: 
# SciPy, scikit learn, TensorFlow, Keras, NumPy, Matplotlib, seaborn, pandas, PyTorch

# LIBRERÍAS, MÓDULOS Y FUNCIONES
# Librerías: conjunto de funciones que ofrece una interfaz bien definida para la funcionalidad que se invoca.
# Módulos: una porción de un programa global. Un módulo debe realizar, comúnmente, una o unas de las tareas del programa.
# Funciones: Son porciones de código que resuelven cosas muy concretas.

# Una librería es un conjunto de módulos cuya agrupación tiene una finalidad específica. 
# Y un módulos, a la vez, está compuesto por un número de funciones para resolver problemas específicos.

# LIBRERÍAS         -> enviar cohetes a Marte
#     |
#     MÓDULOS       -> despegue
#        |          -> aterrizaje
#        |
#        FUNCIONES  -> encender
#                   -> apagar
#                   -> ...

import math
print(math.pi)


import math as M
print(M.pi)


from math import pi
print(pi)


from math import *
print(type(pi))
print(pi)


from pandas import Series
print(Series.index)
