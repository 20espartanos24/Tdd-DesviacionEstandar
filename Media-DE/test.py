# test_calculadora_estadistica.py
import unittest
from funciones import calcular_media, calcular_desstan

class TestCalculadoraEstadistica(unittest.TestCase):

    def test_calcular_media_con_enteros(self):
        total=0
        print("------------Calcular media aritmetica------------")
        cantidad_valores = int(input(" Ingrese la lista de numeros para hallar la media: "))
        lista_datos=[]
        for i in range(cantidad_valores):
            value= float(input(f" Introduce el valor {i+1}:"))
            lista_datos.append(value)
            total+=1
        
        esperado = 3.0
        self.assertAlmostEqual(calcular_media(lista_datos), esperado, places=7)
        

    def test_calcular_desviacion_estandar_con_enteros(self):
        total=0
        print("------------Calcular desviacion estandar------------")
        cantidad_valores = int(input(" Ingrese la lista de numeros : "))
        lista_datos=[]
        for i in range(cantidad_valores):
            value= float(input(f" Introduce el valor {i+1}:" ))
            lista_datos.append(value)
            total+=1
        esperado = 1.4142135623730951 
        self.assertAlmostEqual(calcular_desstan(lista_datos), esperado, places=7)

if __name__ == '__main__':
    unittest.main()
