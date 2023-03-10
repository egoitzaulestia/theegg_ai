"""
FUNCIONES EN PYTHON
Existen 4 tipos de funciones Python:
    1. Las que NO reciben ningún parámetro y NO devuelven un resultado.
    2. Las que NO reciben ningún parámetro y SÍ devuelven un resultado.
    3. Las que Sí reciben algún parámetro y NO devuelven un resultado.
    4. Las que SÍ reciben algún parámetro y SÍ devuelven un resultado.
"""

# 1. Funciones que NO reciben y NO devuelven

# Defino la función
# Una función que NO recibe ningún parámetro y NO devuelve ningún valor.
def mi_funcion():
    print("Soy una sencilla función. Simplemente escribo. Soy así.")

# Llamamos a la función
mi_funcion()


# 2. Funciones que NO reciben y SÍ devuelven

# Esta función NO recoge ningún parámetro pero SÍ devuelve un valor
def devuelve_valor():
    cadena = "The Egg es de 10"
    return cadena

# Recoge el valor que le devuelve la función
# y se lo asigna a la variable recoger
recoger = devuelve_valor()
print(recoger)


# 3. Funciones que SÍ reciben y NO devuelven

# Esta función recibe 3 números y escribe el mayor de todos
def maxNum(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print("Son iguales")

# Llamamos a la función pasándole n parámetros
maxNum(1, 2, 3)


# 4. Funciones que SÍ reciben y SÍ devuelven

# La función recibe un texto y mediante un for cuenta el número
# de caracteres. Después devuelve el resultado
def longitud(param):
    cont = 0
    for z in param:
        cont += 1
    return cont

# El resultado recogido se asigna a la variable retorno
retorno = longitud("Previsión del tiempo para esta noche: estará oscuro")
print(retorno)
