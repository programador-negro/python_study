import unittest

# aqui se escriben las funciones propias
def suma(num_1, num_2):
    return abs(num_1) + num_2

def multiplicacion(n1, n2, n3): # DANIEL
    return n1*n2**n3

# Luego:
# se define la clase que realizara las pruebas
class CajaNegraTest(unittest.TestCase):

    # def test_suma_dos_positivos(self):
    #     '''
    #     * probar que la suma de dos numeros sea igual a 15

    #     * parametro int num_1 cualquier entero
    #       parametro int num_2 cualquier entero
        
    #     * return int 15
    #     '''
    #     num_1 = 10
    #     num_2 = 5

    #     resultado = suma(num_1, num_2) # se almacena el resultado

    #     self.assertEqual(resultado, 15) # se valida el resultado propuesto Vs el esperado.

    # def test_suma_dos_negativos(self):
    #     num_1 = -10
    #     num_2 = -7

    #     resultado = suma(num_1, num_2)

    #     self.assertEqual(resultado, -17)

    def test_multiplicacion_tres_numeros(self): # DANIEL
        n1 = 10
        n2 = 20
        n3 = 30

        resultado = multiplicacion(n1, n2, n3)

        self.assertEqual(resultado, 10737418240000000000000000000000000000000)

if __name__ == '__main__':
    unittest.main()

