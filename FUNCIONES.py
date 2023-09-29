def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    try:
        num_usuario = int(input("Ingresa un numero entero: "))
        if es_primo(num_usuario):
            print(f"{num_usuario} Es un numero primo.")
        else:
            print(f"{num_usuario} No es un numero primo.")
    except ValueError:
        print("Valor invalido. Favor de ingresar un numero entero.")

#---------------------------------------------

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def siguiente_primo(n):
    if n <= 1:
        n = 2
    else:
        n += 1

    while True:
        if es_primo(n):
            return n
        n += 1

if __name__ == "__main__":
    try:
        entrada_usuario = int(input("Ingrese un número entero: "))
        siguiente_primo_numero = siguiente_primo(entrada_usuario)

        if es_primo(siguiente_primo_numero):
            print(f"El siguiente número primo mayor que {entrada_usuario} es {siguiente_primo_numero} y es primo.")
        else:
            print(f"El siguiente número mayor que {entrada_usuario} es {siguiente_primo_numero}, pero no es primo.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")
#--------------------------------------------

def mediana_de_tres(num1, num2, num3):
    # Ordena los números
    numeros_ordenados = [num1, num2, num3]
    numeros_ordenados.sort()

    # La mediana es el número del medio en la lista ordenada
    return numeros_ordenados[1]

if __name__ == "__main__":
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))

        mediana = mediana_de_tres(num1, num2, num3)
        print(f"La mediana de {num1}, {num2} y {num3} es {mediana}.")
    except ValueError:
        print("Entrada no válida. Por favor ingresa valores numéricos.")

#-------------------------------------------
import random

def generar_contrasena_aleatoria():
    longitud_contrasena = random.randint(7, 10)
    contrasena = ''.join(chr(random.randint(33, 126)) for _ in range(longitud_contrasena))
    return contrasena

if __name__ == "__main__":
    contrasena_aleatoria = generar_contrasena_aleatoria()
    print(f"Contraseña generada de manera aleatoria es: {contrasena_aleatoria}")

#------------------------------------------
def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1 ** 2 + lado2 ** 2) ** 0.5
    return hipotenusa

if __name__ == "__main__":
    try:
        lado1 = float(input("Ingresa la longitud del primer lado más corto: "))
        lado2 = float(input("Ingresa la longitud del segundo lado más corto: "))

        hipotenusa = calcular_hipotenusa(lado1, lado2)
        print(f"La longitud de la hipotenusa es {hipotenusa:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa valores numéricos.")
