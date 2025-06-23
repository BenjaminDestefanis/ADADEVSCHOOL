# ejercicios.py

def suma(a, b):
    # 1.A. SUMA
    # La funcion debe retornar la suma de 2 numeros.
    return 

def es_par(n):
    # 1.B. PAR
    # La funcion debe retornar un booleano de acuerdo si el numero recibido es par o no.
    return 

def invertir_cadena(cadena):
    return cadena[::-1]

def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def contar_vocales(texto):
    return sum(1 for letra in texto.lower() if letra in 'aeiou')

def maximo(lista):
    return max(lista)

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

def cuadrados(lista):
    return [x**2 for x in lista]

def sumar_lista(lista):
    return sum(lista)

def contar_palabra(texto, palabra):
    return texto.lower().split().count(palabra.lower())
