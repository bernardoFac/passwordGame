# Lista de jugadores de Argentina campeona del mundo 2022
jugadores = ["MESSI", "DI MARIA", "DE PAUL", "OTAMENDI", "MARTINEZ", "ALVAREZ", "MAC ALLISTER", "ENZO FERNÁNDEZ", "MOLINA", "ROMERO", "ACUÑA", "TAGLIAFICO", "PAREDES", "PEZZELLA", "RULLI", "ARMANI", "FOYTH", "CORREA", "PALACIOS", "MONTIEL", "GÓMEZ", "DIBU MARTÍNEZ", "LISANDRO MARTÍNEZ"]

def regla1(contraseña):
    return len(contraseña) > 8

def regla2(contraseña):
    for char in contraseña:
        if char.isdigit():
            return True
    return False

def regla3(contraseña):
    suma = sum(int(char) for char in contraseña if char.isdigit())
    return suma <= 25

def regla4(contraseña):
    for char in contraseña:
        if char.isupper():
            return True
    return False

def regla5(contraseña):
    return 'AVION' in contraseña.upper()

def regla6(contraseña):
    for jugador in jugadores:
        if jugador in contraseña.upper():
            return True
    return False

# Lista de reglas con descripciones
reglas = [
    ("Debe tener 8 caracteres.", regla1),
    ("Debe incluir al menos un número.", regla2),
    ("La suma de los números no debe ser mayor a 25.", regla3),
    ("Debe tener al menos una letra mayúscula.", regla4),
    ("Debe contener la palabra 'AVION'.", regla5),
    ("Debe contener el nombre de un jugador de Argentina campeona del mundo 2022.", regla6)
]

# Juego
def jugar_contraseña():
    reglas_aplicadas = []
    ronda = 1
    while True:
        print(f"\nRonda {ronda}: ")
        
        # Mostrar las reglas actuales
        if reglas_aplicadas:
            print("Las reglas actuales son:")
            for i, (descripcion, _) in enumerate(reglas_aplicadas):
                print(f"Regla {i+1}: {descripcion}")
        else:
            print("No hay reglas aplicadas aún.")
        
        # Solicitar una contraseña
        contraseña = input("Introduce una contraseña: ")
        
        # Verificar si cumple con todas las reglas actuales
        cumple_todas = True
        for _, regla in reglas_aplicadas:
            if not regla(contraseña):
                cumple_todas = False
                break
        
        if cumple_todas:
            print("¡Contraseña correcta!")
        else:
            print("La contraseña no cumple con las reglas.")
            continue
        
        # Añadir una nueva regla si quedan reglas por aplicar
        if len(reglas_aplicadas) < len(reglas):
            reglas_aplicadas.append(reglas[len(reglas_aplicadas)])
            print(f"Nueva regla añadida: {reglas_aplicadas[-1][0]}")
        else:
            print("¡Has ganado! Todas las reglas han sido aplicadas.")
            break
        
        ronda += 1

# Iniciar el juego
jugar_contraseña()
