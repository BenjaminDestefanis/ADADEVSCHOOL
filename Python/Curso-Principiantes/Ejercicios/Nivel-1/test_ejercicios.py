# test_ejercicios.py

import unittest
from  colorama import Fore, Style, init
import ejercicios  # Asegúrate de que ambos archivos estén en la misma carpeta

init(autoreset=True)


class TestEjercicios(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(ejercicios.suma(2, 3), 5)

    def test_es_par(self):
        self.assertTrue(ejercicios.es_par(4))
        self.assertFalse(ejercicios.es_par(3))

    def test_invertir_cadena(self):
        self.assertEqual(ejercicios.invertir_cadena("hola"), "aloh")

    def test_factorial(self):
        self.assertEqual(ejercicios.factorial(5), 120)

    def test_contar_vocales(self):
        self.assertEqual(ejercicios.contar_vocales("hola mundo"), 4)

    def test_maximo(self):
        self.assertEqual(ejercicios.maximo([1, 5, 3]), 5)

    def test_es_palindromo(self):
        self.assertTrue(ejercicios.es_palindromo("anita lava la tina"))
        self.assertFalse(ejercicios.es_palindromo("python"))

    def test_cuadrados(self):
        self.assertEqual(ejercicios.cuadrados([1, 2, 3]), [1, 4, 9])

    def test_sumar_lista(self):
        self.assertEqual(ejercicios.sumar_lista([1, 2, 3]), 6)

    def test_contar_palabra(self):
        self.assertEqual(ejercicios.contar_palabra("Hola mundo hola", "hola"), 2)


class TestEjerciciosExtra(unittest.TestCase):

    def test_obtener_mayor(self):
        self.assertEqual(ejercicios.obtener_mayor(5, 9, 3), 9)

    def test_convertir_a_celsius(self):
        self.assertAlmostEqual(ejercicios.convertir_a_celsius(212), 100.0)

    def test_numero_es_primo(self):
        self.assertTrue(ejercicios.numero_es_primo(7))
        self.assertFalse(ejercicios.numero_es_primo(4))

    def test_contar_digitos(self):
        self.assertEqual(ejercicios.contar_digitos(12345), 5)

    def test_suma_digitos(self):
        self.assertEqual(ejercicios.suma_digitos(123), 6)

    def test_encontrar_menor(self):
        self.assertEqual(ejercicios.encontrar_menor([3, 1, 5]), 1)

    def test_duplicar_elementos(self):
        self.assertEqual(ejercicios.duplicar_elementos([1, 2]), [2, 4])

    def test_remover_duplicados(self):
        self.assertEqual(set(ejercicios.remover_duplicados([1, 1, 2])), {1, 2})

    def test_obtener_promedio(self):
        self.assertEqual(ejercicios.obtener_promedio([2, 4, 6]), 4)

    def test_unir_cadenas(self):
        self.assertEqual(ejercicios.unir_cadenas(["hola", "mundo"]), "hola mundo")

if __name__ == '__main__':
    unittest.main()


