"""
Простой калькулятор для демонстрации CI/CD
"""


class Calculator:
    """Класс калькулятора с базовыми операциями"""
    
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание второго числа из первого"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Деление первого числа на второе"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    def power(self, a: float, b: float) -> float:
        """Возведение числа в степень"""
        return a ** b
