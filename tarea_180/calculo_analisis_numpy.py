# NUMPY es el paquete fundamental para la computación científica en Python.
# Proporciona múltiples funciones par trabajar con arrays y para realizar operaciones rápidas sobre éstas.

# Permite un manejo de datos extremadamente rápido y tiene su propia estructura de datos incorporada.

# Los 4 principales beneficios de NumPy:
# 1_ Más velocidad
# 2_ Menos bucles
# 3_ Código más claro
# 4_ Mejor calidad


# Qué es un ARRAY?
# Un array es una estructura de datos de un mismo tipo organizada de una forma estructurada y compuesta por n dimensiones.
# Las dimensiones de un array también se conocen como ejes y en el caso de Python, las listas, diccinarios o tuplas, son agrupaciones de datos con diferentes particularidades, igual que los array-s.

# 1. 1D array: agrupaciones de datos de 1xn o nx1 dimensiones. Conocidos como vectores.
# 2. 2D array: agrupaciones de datos de mxn o nxm dimensiones. Conocidos como matrices.
# 3. 3D array: agrupaciones de datos de lxmxn dimensiones. Cubos de datos.
# 4. Hasta que la memoria del sistema lo soporte no hay límite para el número de dimensiones.

import numpy as np

a = np.array([2, 4, 6, 8, 10])

# Para saber que tipo de dato es la variable a
print(type(a))

# Para saber que tipo de variables contiene el array
a.dtype 
print(a.dtype)

# Podemos indiacar por qué tipo de variables queremos que se componga el array
a = np.array([2, 4, 8, 10], dtype = float)
print(a.dtype)

# Conversión de tipos de variable
a.astype(int)
print(a.astype(int))

# Incluso podemos trabajar con variables complejas
a = np.array([2, 4, 6, 8, 10], dtype = complex)
# Saber que tipo de variable contiene a
print(a)


# Array-s especiales

# Matriz vacía (empty): 
# Devuelve un nuevo array con la forma y tipo, pero sin inicializar las entredas.
b = np.empty((2, 2))
print(b) # Para ver el resultado real comentar todos los array-s a
print(b.shape)

# Matriz identidad (identity):
# con numeros enteros y de tamaño nxn
d = np.identity(5).astype(int)
print(d)

# Matriz de ceros (zeros):
# de nxm
e = np.zeros((4, 6))
print(e)

# Matriz de unos (ones):
# de nxm
f = np.ones((3, 4))
print(f.shape)


# función linspace (start, stop, num=n)
h = np.linspace(0, 2, num=10)
print(h)

# funcion arange (start, stop, step)
# en este caso no metemos el paso (step) aunque sí indicamos el tipo de variable
i = np.arange(0, 5, dtype = int)
print(i)


# Funciones matemáticas y constantes

# Números especiales
print(np.e)
print(np.pi)

# Logaritmos
np.log(1)
print(np.log(1))

# Operaciones entre array-s: por ejemplo la suma de 2 matricies identidad
i = np.identity(5).astype(int)
j = np.identity(5).astype(int)
k = i + j
print(k)

# Raices cuadradas de un vector, matriz, cubo
l = np.array([9, 9, 9], dtype = int)
print(l)
m = np.sqrt(l)
print(m)

# Operaciones booleanas entre posiciones de diferentes matrices
print(l < m)

var = [[2, 3, 4], [5, 6, 7]]
print(var[0][2])
print(var[1][2])
