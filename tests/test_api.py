"""
Тесты для Flask API
"""
import pytest
from app.api import app


@pytest.fixture
def client():
    """Фикстура для тестового клиента Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Тесты для эндпоинта health"""
    
    def test_health_check(self, client):
        """Тест health check эндпоинта"""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'calculator-api'
        assert 'version' in data


class TestCalculateEndpoint:
    """Тесты для эндпоинта calculate"""
    
    def test_addition(self, client):
        """Тест операции сложения через API"""
        response = client.post('/calculate', json={
            'operation': 'add',
            'a': 5,
            'b': 3
        })
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['result'] == 8
        assert data['operation'] == 'add'
    
    def test_division(self, client):
        """Тест операции деления через API"""
        response = client.post('/calculate', json={
            'operation': 'divide',
            'a': 10,
            'b': 2
        })
        assert response.status_code == 200
        assert response.get_json()['result'] == 5
    
    def test_division_by_zero(self, client):
        """Тест деления на ноль через API"""
        response = client.post('/calculate', json={
            'operation': 'divide',
            'a': 10,
            'b': 0
        })
        assert response.status_code == 400
        assert 'error' in response.get_json()
    
    def test_missing_operation(self, client):
        """Тест запроса без указания операции"""
        response = client.post('/calculate', json={
            'a': 5,
            'b': 3
        })
        assert response.status_code == 400
        assert 'Операция не указана' in response.get_json()['error']
    
    def test_missing_operands(self, client):
        """Тест запроса с недостающими операндами"""
        response = client.post('/calculate', json={
            'operation': 'add',
            'a': 5
        })
        assert response.status_code == 400
    
    def test_invalid_operands(self, client):
        """Тест с некорректными операндами"""
        response = client.post('/calculate', json={
            'operation': 'add',
            'a': 'not_a_number',
            'b': 3
        })
        assert response.status_code == 400
    
    def test_unknown_operation(self, client):
        """Тест с неизвестной операцией"""
        response = client.post('/calculate', json={
            'operation': 'unknown',
            'a': 5,
            'b': 3
        })
        assert response.status_code == 400
        assert 'Неизвестная операция' in response.get_json()['error']
    
    def test_no_json_data(self, client):
        """Тест запроса без JSON"""
        response = client.post('/calculate')
        assert response.status_code == 415
