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

if __name__ == '__main__':
    unittest.main()
    """ suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestEjercicios)
    runner = unittest.TextTestRunner(resultclass=lambda *args, **kwargs: ColorResult(*args, **kwargs))
    runner.run(suite) """


