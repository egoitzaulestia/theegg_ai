# THE EGG
# TAREA 176
# Módulos / Python, programación para IA / Flujos de control de un programa

# Problemas mediante la utilización de controladores de flujo

# 1. Programa que diga el máximo de 3 números dados
a = 23
b = 89
c = 52

if a > b:
    if a > c:
        print("a es el mayor número.")
elif b > a:
    if b > c:
        print("b es el mayor número.")
else:
    print("c es el mayor número.")


# 2. Programa que diga la longitud de una frase
frase = input("Escribe una frase: ")
longitud = len(frase)
print(f"La longitud de la frase es: {longitud}")


# 3. Programa que determine si un carácter previamente dado es vocal o no
char = input("Introduce un carácter: ")
vocales = ["a", "e", "i", "o", "u"]

if char in vocales:
    print(f"El carácter \"{char}\" es una vocal")
else:
    print(f"El carácter \"{char}\" no es una vocal")
    

# 4. Programa que sume los valores de una lista
valores = [2, 5, 64, 92, 1]
total = 0

for i in valores:
    total = total + i
print(f"La suma total de la lista es: {total}")


# 5. Programa que diga si una palabra dada es palíndromo
word = input("Introduce una palabra: ")

if word == word[::-1]:
    print(f"\"{word}\" es un palíndromo.")
else:
    print(f"\"{word}\" no es un palíndromo.")


# 6. Programa que compare dos listas y encuentre si hay algún valor coincidente
contenedor1 = [2, "ant", 32, 432, "Xerox"]
contenedor2 = [64, 632, "z", "Xerox", "sgf00"]
coincidente = []

for valor in contenedor1:
    if valor in contenedor2:
        coincidente.append(valor)

if coincidente:
    print(f"Hay valores coincidentes: {coincidente}")
else:
    print(f"No hay coincidentes.")
