# Programa para calcular la superficie de un cuadrado conociendo el valor de un lado.

# Pedimos al usuario que introdusca el valor de uno de los lados del cuadrado
# y asignamos el valor introducido del usuario a la variable "lado"
lado = float(input("Introduce el valor de uno de los lados del cuadrado: "))
area = lado * 2 # Multiplicamos por 2 el valor de "lado"
print(f"La superficie del cuadrado es {lado:.2f}") # Mostramos el resultado
