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
    # 1.C. INVERTIR
    # La funcion recibe un string, y deve devolverlo invertido.
    return 

def factorial(n):
    # 1.D. FACTORIAL
    # La funcion recibe un numero, y debe retornar el factorial de ese numero.
    return

def contar_vocales(texto):
    # 1.E. CONTADOR VOCALES
    # La funcion recibe un string, y debe retornar la CANTIDAD de vocales.
    return

def maximo(lista):
    # 1.F. MAXIMO
    # La funcion recibe un lista que contiene numeros, debe retornar el numero mas grande de la lista.
    return

def es_palindromo(cadena):
    # 1.G. PALINDROMO
    # Debe retornar un booleano de acuerdo si la palabra es palindromo
    return 

def cuadrados(lista):
    # 1.H. CUADRADOS
    # La funcion recibe una lista y debe retornar una lista con el valor de cada numero elevado al cuadrado.
    return

def sumar_lista(lista):
    # 1.I. SUMA LISTA
    # La funcion recibe una lista con numeros, y debe retornar la suma de todos los numeros.
    return

def contar_palabra(texto, palabra):
    # 1.J. CONTADOR PALABRAS
    # Falta analizar para definir
    return texto.lower().split().count(palabra.lower())

# ------------------------ SECCION 2

def obtener_mayor(a, b, c):
    # 1.K. OBTENER MAYOR
    # La funcion recibe 3 numeros, debe retornar el mayor.
    return 

def convertir_a_celsius(fahrenheit):
    # 1.H. CONVERTOR A CELSIUS
    # La funcion recive un numero en grados fahrenheit, debe retornar el el valor en celcius 
    return

def numero_es_primo(n):
    # 1.I. NUMERO PRIMO
    # La funcion recibe un numero, debe retornar un booleano de acuerdo si el numero es o no primo.
    return

def contar_digitos(numero):
    return len(str(abs(numero)))

def suma_digitos(numero):
    return sum(int(d) for d in str(abs(numero)))

def encontrar_menor(lista):
    return min(lista)

def duplicar_elementos(lista):
    return [x * 2 for x in lista]

def remover_duplicados(lista):
    return list(set(lista))

def obtener_promedio(lista):
    return sum(lista) / len(lista)

def unir_cadenas(lista_cadenas):
    return " ".join(lista_cadenas)
