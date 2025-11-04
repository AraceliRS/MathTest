import unittest
from math_stats import *
#pytests

class TestStats(unittest.TestCase):

    #Tests para add(), tiene mensaje de error personalizado
    def test_add(self):
        #1. setup
        a,b = 2,12
        #2. expected outputs
        res = 14
        #3. assert
        self.assertEqual(add(a,b),res, "COMO SUMASTE MAL") 
        #prueba que se sume correctamente con numeros negativos 
        self.assertEqual(add(1,-2),-1, "COMO SUMASTE MAL") 


    #Tests para substract(), tiene mensaje de error personalizado
    def test_substract(self):
        #1. setup
        a,b = 2,12
        #2. expected outputs
        res = -10
        #3. assert

        #Prueba con números positivos
        self.assertEqual(subtract(a,b),res, "COMO RESTASTE MAL")
        self.assertEqual(subtract(5,2),3, "COMO RESTASTE MAL")
        #Prueba con números negativos
        self.assertEqual(subtract(5,-2),7, "COMO RESTASTE MAL")

    #Tests para power(), se utilizó TDD (pruebas definidas antes del código)
    def test_power(self):
        #Valores Exactoos
        self.assertEqual(power(1,2),1)
        self.assertEqual(power(2,2),4)
        self.assertEqual(power(2,-1),0.5)
        self.assertEqual(power(5,-3),1/125)
        #Al ser un número decimal se hace una aproximación y da un margen de error del 0.01
        self.assertAlmostEqual(power(3,-1),0.33,delta=0.01)

   # Tests para multiply()
    def test_multiply(self):
        #Multiplicaciones básicas
        self.assertEqual(multiply(3, 6), 18)
        self.assertEqual(multiply(1, 6), 6)
        #Pruebas con negativos
        self.assertEqual(multiply(1, -1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        
  #Tests para divide()
    def test_divide(self):
        # División normal y con negativos
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(8, -2), -4)
        self.assertEqual(divide(0, 5), 0) 

    def test_divideRaise(self):
    #Lanzar error al dividir entre 0
        with self.assertRaises(ValueError):
            divide(2, 0)

  #Tests para square_root()
    def test_square_root(self):
        # Raíces exactas
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(1), 1)
        #Raíz aproximada
        self.assertAlmostEqual(square_root(12), 3.464, delta=0.01)
    
   
    def test_square_rootRaise(self):
     #Verifica que square_root() lance error con número negativo
        with self.assertRaises(ValueError):
            square_root(-5)
    
    #Tests para absolute_value()
    def test_absolute_value(self):
        self.assertEqual(absolute_value(1),1)
        self.assertEqual(absolute_value(-1),1)
        self.assertEqual(absolute_value(-10.5),10.5)
    
    #Tests para mean()
    def test_mean(self):
        self.assertEqual(mean([1,1,1,1]),1)
        self.assertEqual(mean([1,5,-2]),4/3)
        self.assertEqual(mean([1,5,5,100,20]),26.2)


    def test_meanRaise(self):
        #Lanzar error con lista vacia
        with self.assertRaises(ValueError):
            mean([])

    #Test para median()
    def test_median(self):
        #Pruebas con listas impares y pares
        self.assertEqual(median([1,1,1,1,1]),1)
        self.assertEqual(median([1,3,2,2]),2)
        self.assertEqual(median([50,3,8,7,65,24]),16)


    def test_medianRaise(self):
    #Lanzsar error con lista vacia
        with self.assertRaises(ValueError):
            median([])

    #Tests para mode()
    def test_mode(self):
        self.assertEqual(mode([5,5,5,5,1]),5)
        #Multiples modas
        self.assertEqual(mode([1,1,1,3,3,3,4]),[1,3])
        #Ninguna moda
        self.assertEqual(mode([1,2,3]),None)
        self.assertEqual(mode([1,2,1,2]),None)

    
    def test_modeRaise(self):
    #Lanzar error con lista vacia
        with self.assertRaises(ValueError):
            mode([])
    
    #Test para variance()
    #Considera que es varianza poblacional y NO muestral
    def test_variance(self):
        #Utiliza valores aproximados con margen de error del 0.01
        self.assertAlmostEqual(variance([600,470,170,430,300]),21704,delta=0.01)
        self.assertAlmostEqual(variance([10,34,23,54,9]),280.4,delta=0.01)
        self.assertAlmostEqual(variance([6,3,2,1]),3.5,delta=0.01)

    def test_varianceRaise(self):
        #Lanzar error con lista vacia
        with self.assertRaises(ValueError):
            variance([])

    #Test para standard_deviation
    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([600,470,170,430,300]),147.32, delta=0.01)
        self.assertAlmostEqual(standard_deviation([10,34,23,54,9]),16.74,delta=0.01)
        self.assertAlmostEqual(standard_deviation([6,3,2,1]),1.8708,delta=0.01)

    def test_standard_deviationeRaise(self):
         #Lanzar error con lista vacia
        with self.assertRaises(ValueError):
            standard_deviation([])

    #Tests para is_even()
    def test_is_even(self):
        #Son par
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(20002))
        #Son impar
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(21))
        #Considera que los flotantes no pueden ser par o impar
        self.assertFalse(is_even(1.12))


    #Tests para is_prime()
    def test_is_prime(self):
        #No son primos
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(8))
        #Son primos
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        #Considera que los flotantes no pueden ser primos
        self.assertFalse(is_prime(1.12))
        
    #Tests para factorial()
    def test_factorial(self):
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(5),120)

    def test_factorialRaise(self):
        #Lanzar error si es negativo
        with self.assertRaises(ValueError):
            factorial(-1)


    #Tests para gcd() 
    #Máximo Comun divisor
    def test_gdc(self):
        self.assertEqual(gcd(1,1),1)
        self.assertEqual(gcd(16,12),4)
        self.assertEqual(gcd(123,54),3)
        #Considera negativos
        self.assertEqual(gcd(-123,54),3)
        #Ya que se usa el algoritmo de Euclediano, es correcto
        self.assertEqual(gcd(3,7),1)




if __name__ == "__main__":
    print("Hola")
    unittest.main()