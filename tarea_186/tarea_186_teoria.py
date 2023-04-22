# Python tiene una serie de funciones (Built-in)

# abs(), retorna el valor absoluto de un número
print(abs(-3))

# float(), retorna un decimal o punto flotante a partir de un número o una cadena.
print(float(3))

# input(), lee una entrada que introduce el usuario y la convierte en una cadena.
input("Introduce tu nombre: ")

# len(), retorna el elmento mayor en un interable o el mayor de dos o más argumentos.
len("Nunca me siento tan solo como cuando necesito ponerme crema solar en la espalda.")

# max(), retorna el elemento mayor en un iterable o mayor de dos o más argumentos.
max(4, 55, 123)

meses = ["enero", "febrero", "marzo"]
max(meses)

# print(), imprime el objeto en una cadena.
print("La edad es algo que no importa, a menos que sea usted un queso")

# range(), lista inmutable de números enteros en sucesión aritmética
""" En este caso metemos range() dentro de list(.
Utilizamos 2 funciones integradas, una dentro de otra. """
list(range(10))

for num in range(10, 0, -2):
    print(num)

# sum(), nos devuleve la suma los elementos de entrada.
numeros = [12, 67, 2, 68, 85, 65]
sum(numeros)


# NO REINVENTES LA RUEDA

# A mano
def longitud(param):
    kont = 0
    for z in param:
        kont += 1 
    return kont

retorno = longitud("Nunca dejes para mañana lo que puedas hacer pasado mañana")
print(retorno)

print(len("Nunca dejes para mañana lo que puedas hacer pasado mañana"))
