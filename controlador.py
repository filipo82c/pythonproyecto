def solotexto(prompt):
    while True:
        texto = input(prompt).strip()
        if texto:
            return texto
        print("Entrada invalida. Por favor, ingrese solo letras.")
def solonumeros(prompt):
    while True:
        texto = input(prompt).strip()
        if texto.isdigit():
            return texto
        print("Entrada invalida. Por favor, ingrese solo numeros.")