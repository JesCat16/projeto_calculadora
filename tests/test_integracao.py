import unittest
from src.calculadora import Calculadora

class Test_Integracao(unittest.TestCase):
    """
    teste de operação sequencial
    """
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        calc.somar(2,3)
        resultado1 = calc.obter_ultimo_resultado()

        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()

        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()

        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)

    """
    teste de interface entre métodos
    """
    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2,3)
        calc.somar(calc.obter_ultimo_resultado(), 2)

        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico),2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

if __name__ == '__main__':
    unittest.main()