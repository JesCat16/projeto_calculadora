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
        """
        String no lugar de numero na subtração
        """
        with self.assertRaises(TypeError):
            self.calc.subtrair("5", 3)   

    def test_tipagem_invalida_subtracao_none(self):
        """
        None no lugar de numero na subtração
        """
        with self.assertRaises(TypeError):
            self.calc.subtrair(5, None)  

    def test_tipagem_invalida_subtracao_boolean(self):
        """
        Boolean no lugar de numero na subtração
        """
        with self.assertRaises(TypeError):
            self.calc.subtrair(5, True)   

    def test_tipagem_invalida_multiplicar_string(self):
        """
        String no lugar de numero na multiplicação
        """
        with self.assertRaises(TypeError):
            self.calc.multiplicar("5", 3)  

    def test_tipagem_invalida_multiplicar_none(self):
        """
        None no lugar de numero na multiplicação
        """
        with self.assertRaises(TypeError):
            self.calc.multiplicar(5, None) 

    def test_tipagem_invalida_multiplicar_boolean(self):
        """
        Boolean no lugar de numero na multiplicação
        """
        with self.assertRaises(TypeError):
            self.calc.multiplicar(5, True)  

    def test_tipagem_invalida_dividir_string(self):
        """
        String no lugar de numero na divisão
        """
        with self.assertRaises(TypeError):
            self.calc.dividir("5", 3) 

    def test_tipagem_invalida_dividir_none(self):
        """
        None no lugar de numero na divisão
        """
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)  

    def test_tipagem_invalida_dividir_boolean(self):
        """
        Boolean no lugar de numero na divisão
        """
        with self.assertRaises(TypeError):
            self.calc.dividir(5, True)  # 

    def test_consistencia_historico_1(self):
        """
        Verifica a consistência dos dados depois de uma operação
        """
        self.calc.subtrair(3, 2)
        self.assertEqual(len(self.calc.historico), 1)
        self.assertIn("3 - 2 = 1", self.calc.historico)

    def test_consistencia_historico_2(self):
        """
        Verifica a consistência dos dados depois de duas operações
        """
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        self.assertEqual(len(self.calc.historico), 2)
        self.assertIn("2 + 3 = 5", self.calc.historico)
        self.assertIn("4 * 5 = 20", self.calc.historico)
    
    def test_inicialização(self):
        """
        Garante que a inicialização foi feita corretamente
        """
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    def test_modificacao_historico_soma(self):
        """
        Valida a inserção de informações e exclusão de informação no histórico quando
        realizada a soma
        """
        calc = Calculadora()
        calc.somar(1 , 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    def test_modificacao_historico_subtracao(self):
        """
        Valida a inserção de informações e exclusão de informação no histórico quando
        realizada a subtração
        """
        calc = Calculadora()
        calc.subtrair(1 , 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    def test_modificacao_historico_divisao(self):
        """
        Valida a inserção de informações e exclusão de informação no histórico quando
        realizada a divisão
        """
        calc = Calculadora()
        calc.dividir(1 , 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    
    def test_modificacao_historico_multiplicacao(self):
        """
        Valida a inserção de informações e exclusão de informação no histórico quando
        realizada a multiplicação
        """
        calc = Calculadora()
        calc.multiplicar(1 , 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    
    def test_modificacao_historico_potencializacao(self):
        """
        Valida a inserção de informações e exclusão de informação no histórico quando
        realizada a potencialização
        """
        calc = Calculadora()
        calc.potencia(1 , 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    
    def test_limite_inferior(self):
        """
        Teste de comportamento com valores minimos
        """
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0,5)
        self.assertEqual(resultado, 5)
        # Teste com números negativos muito pequenos
        resultado = calc.multiplicar(-1e-10 , 2)
        self.assertEqual(resultado , -2e-10)

    def test_divisao_por_zero(self):
        """
        Valida a impossibilidade de dividir por 0
        """
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10,0)

    def test_mensagem_erro_soma(self):
        """
        Valida mensagem de erro da soma
        """
        calc = Calculadora()
        try:
            calc.somar(5, "1")
        except ValueError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")
        
    def test_mensagem_erro_subtracao(self):
        """
        Valida mensagem de erro da subtração
        """
        calc = Calculadora()
        try:
            calc.subtrair(5, "1")
        except ValueError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")

    def test_mensagem_erro_multiplicacao(self):
        """
        Valida mensagem de erro da multiplicação
        """
        calc = Calculadora()
        try:
            calc.multiplicar(5, "1")
        except ValueError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")

    def test_mensagem_erro_divisao(self):
        """
        Valida mensagem de erro da divisão
        """
        calc = Calculadora()
        try:
            calc.dividir(5, "1")
        except ValueError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")
        
    def test_mensagem_erro_potencia(self):
        """
        Valida mensagem de erro da potência
        """
        calc = Calculadora()
        try:
            calc.potencia(5, "1")
        except ValueError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")
        
    def test_mensagem_erro_div0(self):
        calc = Calculadora()
        try:
            calc.dividir(5 ,0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")