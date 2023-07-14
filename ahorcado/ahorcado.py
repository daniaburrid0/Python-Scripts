import random

# Lista de palabras para elegir
palabras = ["manzana", "platano", "cereza", "fecha", "saúco", "higo", "uva"]

# Seleccionar una palabra al azar de la lista
palabra = random.choice(palabras)

# Crear una lista de guiones bajos para representar la palabra oculta
palabra_oculta = ["_"] * len(palabra)

# Llevar un registro del número de intentos incorrectos
intentos_incorrectos = 0

# Llevar un registro de las letras que se han adivinado
letras_adivinadas = []

# Repetir hasta que se adivine la palabra o el jugador se quede sin intentos
while "_" in palabra_oculta and intentos_incorrectos < 6:
    # Imprimir el estado actual del juego
    print(" ".join(palabra_oculta))
    print(f"Intentos incorrectos: {intentos_incorrectos}")
    print(f"Letras adivinadas: {', '.join(letras_adivinadas)}")

    # Pedir al jugador que adivine una letra
    adivinanza = input("Adivina una letra: ").lower()

    # Comprobar si la letra ya se ha adivinado
    if adivinanza in letras_adivinadas:
        print(f"Ya adivinaste la letra '{adivinanza}'")
        continue

    # Comprobar si la adivinanza es una letra
    if not adivinanza.isalpha() or len(adivinanza) != 1:
        print("Por favor, introduce una letra válida.")
        continue

    # Añadir la letra a la lista de letras adivinadas
    letras_adivinadas.append(adivinanza)

    # Comprobar si la letra está en la palabra
    if adivinanza in palabra:
        # Reemplazar los guiones bajos con la letra adivinada
        for i in range(len(palabra)):
            if palabra[i] == adivinanza:
                palabra_oculta[i] = adivinanza
    else:
        # Incrementar el número de intentos incorrectos
        intentos_incorrectos += 1
        print(f"La letra '{adivinanza}' no está en la palabra.")

# Comprobar si el jugador ganó o perdió
if "_" not in palabra_oculta:
    print(f"¡Ganaste! La palabra era '{palabra}'.")
else:
    print(f"¡Perdiste! La palabra era '{palabra}'.")