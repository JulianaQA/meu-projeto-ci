import pytest
from src.calculadora import Calculadora

class TestCalculadora:
    def setup_method(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        assert self.calc.somar(2, 3) == 5
        assert self.calc.somar(-1, 1) == 0
        assert self.calc.somar(0, 0) == 0
    
    def test_subtrair(self):
        assert self.calc.subtrair(5, 3) == 2
        assert self.calc.subtrair(0, 5) == -5
    
    def test_multiplicar(self):
        assert self.calc.multiplicar(2, 3) == 6
        assert self.calc.multiplicar(-2, 3) == -6
        assert self.calc.multiplicar(0, 5) == 0
    
    def test_dividir(self):
        assert self.calc.dividir(6, 2) == 3
        assert self.calc.dividir(5, 2) == 2.5
        
    def test_dividir_por_zero(self):
        with pytest.raises(ValueError, match="Divisão por zero não permitida"):
            self.calc.dividir(10, 0)