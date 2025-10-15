"""
Flask API для калькулятора
"""
from flask import Flask, request, jsonify
from app.calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/health', methods=['GET'])
def health():
    """Проверка работоспособности сервиса"""
    return jsonify({
        'status': 'healthy',
        'service': 'calculator-api',
        'version': '1.0.0'
    }), 200


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Выполнение математических операций
    
    Ожидаемый формат запроса:
    {
        "operation": "add|subtract|multiply|divide|power",
        "a": число,
        "b": число
    }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Требуется JSON'}), 400
    
    operation = data.get('operation')
    a = data.get('a')
    b = data.get('b')
    
    # Валидация входных данных
    if not operation:
        return jsonify({'error': 'Операция не указана'}), 400
    
    if a is None or b is None:
        return jsonify({'error': 'Требуются оба операнда (a и b)'}), 400
    
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({'error': 'Операнды должны быть числами'}), 400
    
    # Выполнение операции
    try:
        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        elif operation == 'power':
            result = calc.power(a, b)
        else:
            return jsonify({'error': f'Неизвестная операция: {operation}'}), 400
        
        return jsonify({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        }), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
