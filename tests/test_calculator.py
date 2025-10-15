"""
Тесты для класса Calculator
"""
import pytest
from app.calculator import Calculator


@pytest.fixture
def calculator():
    """Фикстура для создания экземпляра калькулятора"""
    return Calculator()


class TestCalculator:
    """Набор тестов для калькулятора"""
    
    def test_add_positive_numbers(self, calculator):
        """Тест сложения положительных чисел"""
        assert calculator.add(2, 3) == 5
        assert calculator.add(10, 15) == 25
    
    def test_add_negative_numbers(self, calculator):
        """Тест сложения отрицательных чисел"""
        assert calculator.add(-5, -3) == -8
        assert calculator.add(-10, 5) == -5
    
    def test_subtract(self, calculator):
        """Тест вычитания"""
        assert calculator.subtract(10, 3) == 7
        assert calculator.subtract(5, 10) == -5
    
    def test_multiply(self, calculator):
        """Тест умножения"""
        assert calculator.multiply(3, 4) == 12
        assert calculator.multiply(-2, 5) == -10
        assert calculator.multiply(0, 100) == 0
    
    def test_divide(self, calculator):
        """Тест деления"""
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self, calculator):
        """Тест деления на ноль"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calculator.divide(10, 0)
    
    def test_power(self, calculator):
        """Тест возведения в степень"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 2) == 25
        assert calculator.power(10, 0) == 1
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (0, 0, 0),
        (100, 200, 300),
        (-50, 50, 0),
    ])
    def test_add_parametrized(self, calculator, a, b, expected):
        """Параметризованный тест сложения"""
        assert calculator.add(a, b) == expected
