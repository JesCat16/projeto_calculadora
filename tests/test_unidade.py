import unittest
from src.calculadora import Calculadora


class TesteUnitarioCalcula(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_entrada_saida_soma(self):
        """
        teste de entrada e saida da operação soma
        """
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_entrada_saida_subtracao(self):
        """
        teste de entrada e saida da operação subtração
        """
        resultado = self.calc.subtrair(10, 3)
        self.assertEqual(resultado, 7)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 7)

    def test_entrada_saida_multiplicar(self):
        """
        teste de entrada e saida da operação multiplicação
        """
        resultado = self.calc.multiplicar(5, 2)
        self.assertEqual(resultado, 10)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)

    def test_entrada_saida_divisao(self):
        """
        teste de entrada e saida da operação divisão
        """
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 5)

    def test_entrada_saida_potencia(self):
        """
        teste de entrada e saida da operação potência
        """
        resultado = self.calc.potencia(10, 2)
        self.assertEqual(resultado, 100)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 100)

    def test_tipagem_invalida_soma_string(self):
        """
        teste de tipagem invalida string no lugar de numero soma
        """
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)  # String no lugar de numero na soma

    def test_tipagem_invalida_soma_none(self):
        """
        teste de tipagem invalida string no lugar de numero none
        """
        with self.assertRaises(TypeError):
            self.calc.somar(5, None)  # None no lugar de numero na soma

    def test_tipagem_invalida_soma_boolean(self):
        """
        teste de tipagem invalida string no lugar de numero none
        """
        with self.assertRaises(TypeError):
            self.calc.somar(5, True)  # Boolean no lugar de numero na soma

    def test_tipagem_invalida_subtracao_string(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair("5", 3)  # String no lugar de numero na subtração

    def test_tipagem_invalida_subtracao_none(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(5, None)  # None no lugar de numero na subtração

    def test_tipagem_invalida_subtracao_boolean(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(5, True)  # Boolean no lugar de numero na subtração

    def test_tipagem_invalida_multiplicar_string(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar("5", 3)  # String no lugar de numero na multiplicação

    def test_tipagem_invalida_multiplicar_none(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar(5, None)  # None no lugar de numero na multiplicação

    def test_tipagem_invalida_multiplicar_boolean(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar(
                5, True
            )  # Boolean no lugar de numero na multiplicação

    def test_tipagem_invalida_dividir_string(self):
        with self.assertRaises(TypeError):
            self.calc.dividir("5", 3)  # String no lugar de numero na divisão

    def test_tipagem_invalida_dividir_none(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)  # None no lugar de numero na divisão

    def test_tipagem_invalida_dividir_boolean(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(5, True)  # Boolean no lugar de numero na divisão

    def test_consistencia_historico_1(self):
        self.calc.subtrair(3, 2)
        self.assertEqual(len(self.calc.historico), 1)
        self.assertIn("3 - 2 = 1", self.calc.historico)

    def test_consistencia_historico_2(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        self.assertEqual(len(self.calc.historico), 2)
        self.assertIn("2 + 3 = 5", self.calc.historico)
        self.assertIn("4 * 5 = 20", self.calc.historico)
