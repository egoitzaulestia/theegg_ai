# Variables LOCALES y GLOBALES

# ejemplo de variable local
def hello_1():
    x = "Hello World LOCAL VARIABLE" # variable local
    print(x)

hello_1()


# ejemplo de variable global
def hello_2():
    print(y)

y = "Fuck Society" # variable global

hello_2()
