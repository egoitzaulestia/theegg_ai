# Módulos tiempo.py

# definiciones de tierra, marte y jupiter para averiguarl a cuantp altura estaría un objeto si introducimos los segunfos de caída de objeto.
def tierra(t):
    z = (1/2) * 9.8 * (int(t) * 2)
    return f"{z:.2f}"

def marte(t):
    z = (1 / 2) * 3.7 * (int(t) * 2)
    return f"{z:.2f}"

def jupiter(t):
    z = (1 / 2) * 24.8 * (int(t) * 2)
    return f"{z:.2f}"
