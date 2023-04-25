"""
FUNCIONES LAMBDA, MAP, FILTER Y REDUCE
Funciones avanzadas en Python

"""
##################
# Función Lambda #
##################

# Las funciones lambda nos permiten definir una función "en una expresión".
# Estas funciones se llaman anónimas (pursto que no las definimos con "def").
# Bien usadas pueden mejorar la lectura de tu código, simplificar y potenciar tus algoritmos.

# lambda x : x.upper()
# keyword (lambda) + argumento (x) : sentencia (x.upper())

# una función estándar
def separar_y_seleccionar(linea):
    fila = linea.split(",")
    celda = fila[1]
    return celda

# la misma función con lambda
lambda linea:linea.split(",")[1]


# Aplicando lambda a un ejercicio
# Compañías en el mercado bursátil

# ID, NOMBRE, VALOR, CATEGORIA, VOLUMEN
companias_csv = ["1, MANZANA, 100, SOFTWARE, 80000", \
                 "2, MACROSOFT, 75, SOFTWARE, 120000", \
                 "3, CARALIBO, 83, SOCIAL, 230000", \
                 "4, PAJARITO, 77, SOCIAL, 67000"]

nombres = []
for item in companias_csv:
    nombres.append((lambda linea:linea.split(",")[1])(item))
print(nombres)

"""
Salida:

[' MANZANA', ' MACROSOFT', ' CARALIBO', ' PAJARITO']

"""

###############
# Función Map #
###############

# Permite crear un mapeo entre una función y un listado de elementos.
# Es decir, recibe como parámetro una función y luego uno o varios listados.

# map(function, iterable)
# Devuelve una lista nueva

"""
    • Si la función que queremos aplicar con map recibe 1 argumento, deberemos usar una lista.
      Si la función recibe 2 argumentos, debemos usar 2 lsitas, etc.
      
    • Cuando digo que luego de la función recibe "uno o varios listados" realmente
      purden ser objetos iterables (generador, sets, tuplas...)
      
    • El resultado no es una lista, realmente duvuelve un objeto "generator" pero el uso más frecuente
      es aplicarle un "list()" y con eso obtenemos el listado final.
      
"""

# Aplicando map() en el ejercicio

# Prescindirmos del bucle for mediante el map()
nombres = list(map(lambda linea:linea.split(",")[1], companias_csv))
print(nombres)

# Saquemos ahora la cantidad de caracteres de cada nombre
longitudes = list(map(len, nombres))
print(longitudes)

# Salida:
# [8, 10, 9, 9]

# Ahora formateamos los nombres con su primera letra en mayúscula
formateado = list(map(lambda x:x.capitalize(), nombres))
print(formateado)

# Atención: Nótese en todos los casos el uso de list sobre map

# Ahora los inversores nos piden calcular la media del precio de acciones de estas compañías.
# Haremos un híbrido entre función normal y el uso de las funciones map y lambda
def promedio_de_lista(lista):
    valores = list(map(lambda x: int(x.split(",")[2]), lista))
    if len(valores) == 0:
        return 0
    else:
        return sum(valores)/len(valores)

print(promedio_de_lista(companias_csv))


##################
# Función Filter #
##################

# Otro de los caso típicos que nos solemos topar como Científicos de Datos es el de filtrar datos
# por algún tipo de condición. En este caso lo que hacemos es quedarnos únicamente con las filas
# que tienen las características que buscamos.

# filter(function, squence)
# Devuelve una lista filtrada

# La función filter() tiene como parámetros una función y después un listado.
# Al igual que map(), la función se evaluará para cada item, pero la diferencia es
# que la respuesta booleana de esa función será lo que defina que se filtre o no esa fila.

# Aplicando filter()

# Ahora queremos saber cuanto es la media de las empresas de software y la de las empresas de redes sociales.
# Y cuáles tienen mejor valoración.

# Primero vamos a separar por categorias y luego resolver estas preguntas.
solo_sw = list(filter(lambda x:x.split(",")[3] == 'SOFTWARE', companias_csv))
print(solo_sw)

# Ahora filtramos en otra variable las compañías de redes sociales
solo_social = list(filter(lambda x: x.split(",")[3] == "SOCIAL", companias_csv))
print(solo_social)

# No estoy seguro que sucede que no da el resultado que The Egg ofrece.
print(promedio_de_lista(solo_sw))
print(promedio_de_lista(solo_social))


# Volvemos con lambda con múltiples variables

# En esta ocasión los inversores nos pide calcular cuál es el valor total de cada compañía.
# A la función lambda le podemos pasar más de una función. Nos ayudaremos mediante map() para ello.

# Creamos una función lambda que recibe 2 parámetros
# En este caso asignamos la función lambda a una variable llamada valor_total_compania
valor_total_compania = lambda x, y: int(x) * int(y)

print(valor_total_compania(10, 20))

# ¿Cómo hacemos para usar la función con map()? (recuerda que gracias a map evitamos el tener que iterar "manualmente" usando <for>).

# La función map necesita una función y luego tantas listas como parámetros recibirá dicha función.
# En nuestro caso, para obtener la valoración de las compañías debemos multiplicar el valor de la acción por su volumen.

# Creamos 2 listas utilizando funciones lambda extrayendo estos valores y con ellos alimentaremos la función map().
val_accion = list(map(lambda x: x.split(",")[2], companias_csv))
qty = list(map(lambda x: x.split(",")[4], companias_csv))

valoraciones = list(map(valor_total_compania, val_accion, qty))
print(valoraciones)

"""
Salida:

[8000000, 9000000, 19090000, 5159000]

"""
# Con esto comprobamos que la compañía CaraLibro es la que mayor valor total tiene


##################
# Función Reduce #
##################

# La función reduce() opera con todos los elementos acumulando los resultados parciales y devuelve un único valor (no una lista).

# reduce(function, squence)
# Devuelve un valor

# Un caso "típico" para entender reduce es el de sumar "todos los elementos".
# Sumaremos la columna de "volumen" de nuestro dataset con reduce:

# La función reduce no está incluida entre las funciones estándar Python por lo que debemos importarla mediante <functools>
from functools import reduce

suma = reduce(lambda x, y: int(x) + int(y), qty)
print(suma)

# Podemos comprobar el resultado usando la propia función de python "sum"
sum(list(map(int,qty)))

print(sum(list(map(int,qty))))


# Aplicando reduce a strings:
# ¿Qué pasa si en vez de utiliza números, utilizamos cadenas de texto?
# Esto nos posibilita poder operar sobre un listado de cadenas y obtener un único valor de salida.

# En este ejemplo crearemos una cadena de salida con los nombres de compañía como un listado de html:
html = "<ul><li>" + reduce(lambda x, y: f"{x}</li><li>{y}", formateado) + "</li></ul>"
print(html)


################
# CONCLUSIONES #
################

# LAMBDA nos permite crear funciones anónimas de una línea, con uno o múltiples parámetros de entrada.
# MAP tiene la ventaja de evitar tener que iterar un listado para aplicar una función a todos sus elementos.
# FILTER permite quedarnos con los elementos de una lista que cumplen una condición (evitando también tener que iterar)
# REDUCE permite realizar una operación -definida por usuario- sobre todos los elementos y acumulando un único resultado final.
